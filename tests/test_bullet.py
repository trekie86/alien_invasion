from unittest import TestCase
from bullet import Bullet
from settings import Settings


class TestBullet(TestCase):

    def setUp(self) -> None:
        self.settings = Settings()
        self.bullet = Bullet(None, self.settings, (0, 1))

    def test_init(self):
        self.assertEqual((0, 1), self.bullet.rect.midtop)
        self.assertEqual(self.settings.bullet_color, self.bullet.color)

    def test_update(self):
        old_y_pos = self.bullet.y
        self.bullet.update()
        new_y_pos = self.bullet.y
        # The bullet is traveling up which reducing the y value
        self.assertGreater(old_y_pos, new_y_pos)
