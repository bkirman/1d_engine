from engine.game_engine import BaseGame
from random import random, uniform
from .util import gameover
import settings
import time


class SpaceLads(BaseGame):
    """SpaceLads: survive as long as possible while alien lads drift down the strip. Hold the button to charge the laser cannon and reach further"""

    def init(self, engine):
        self.player_pos = settings.LED_LENGTH - 1
        self.aliens = []
        self.bullet = None
        self.charging = False
        self.charge_timer = 0
        self.spawn_timer = 0
        self.spawn_interval = 24
        self.alien_step = 0
        self.alien_interval = 4
        self.score = 0

    def update(self, engine, button):
        # Start charging when the button is pressed.
        if button['b'] and not self.charging:
            self.charging = True
            self.charge_timer = 0

        # Increase the charge while the button is held.
        if self.charging and button['b']:
            self.charge_timer += 1

        # Fire the bullet when the button is released.
        if self.charging and not button['b']:
            if self.bullet is None:
                self.bullet = {
                    'pos': self.player_pos,
                    'distance': 0,
                    'max_distance': 8 + min(16, self.charge_timer // 3 * 2),
                    'charge': self.charge_timer,
                    'hue': 0.6,
                }
            self.charging = False
            self.charge_timer = 0

        # Move the bullet upward and remove it when it runs out of range.
        if self.bullet is not None:
            self.bullet['distance'] += 1
            self.bullet['pos'] -= 1

            if self.bullet['pos'] <= 0 or self.bullet['distance'] >= self.bullet['max_distance']:
                self.bullet = None
            else:
                for alien in list(self.aliens):
                    if int(alien['pos']) == int(self.bullet['pos']):
                        self.aliens.remove(alien)
                        self.score += 1
                        self.bullet = None
                        break

        # Spawn a new alien from the top every so often.
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.aliens.append({'pos': 0.0, 'hue': uniform(0.0, 1.0)})
            self.spawn_timer = 0

        # Move aliens slowly down the strip.
        self.alien_step += 1
        if self.alien_step >= self.alien_interval:
            for alien in self.aliens:
                alien['pos'] += 1.0
                if int(alien['pos']) >= self.player_pos:
                    gameover(engine)
                    self.init(engine)
                    return
            self.alien_step = 0

    def draw(self, engine, display):
        for i in range(settings.LED_LENGTH):
            display.set_hsv(i, 0.0, 0.0, 0.0)

        # Draw the player at the bottom, or show the charging bullet at that spot.
        if self.charging:
            charge_brightness = 0.4 + min(0.6, self.charge_timer / 20.0)
            display.set_hsv(self.player_pos, 0.6, 1.0, charge_brightness)
        else:
            display.set_hsv(self.player_pos, 0.3, 1.0, 0.8)

        # Draw aliens as little drifting lights.
        for alien in self.aliens:
            display.set_hsv(int(alien['pos']), alien['hue'], 1.0, 0.6)

        # Draw the bullet with a fading brightness as it travels.
        if self.bullet is not None:
            progress = self.bullet['distance'] / float(self.bullet['max_distance'])
            base_brightness = 0.6 + min(0.4, self.bullet['charge'] / 20.0)
            brightness = max(0.0, base_brightness - progress)
            display.set_hsv(int(self.bullet['pos']), self.bullet['hue'], 1.0, brightness)

        time.sleep(0.05)
