
from typing import TYPE_CHECKING

import
from typingTYPE_CHECKING,  import_checking
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class shipArsenal:
    def __init__(self):
        self.game = game
        self.settings = game.settings
        self.arsenal =pygame.sprite.Group()

        def update_arsenal(self):
            self.arsenal.update()
            self.remove_offscreen_bullets()

            def remove_offscreen_bullets(self):
                for bullet in self.arsenal.copy():
                    if bullet.rect.bottom <= 0:
                        self.arsenal.remove(bullet)

            def draw_arsenal(self):
                for bullet in self.arsenal
                    bullet.draw_bullet()

                    def fire_bullet(self):
                        if len(self.arsenal) < self.settings.bullets_allowed:
                            new_bullet = Bullet(self)
                            self.arsenal.add(new_bullet)
                            return True
                        return False
                    


    