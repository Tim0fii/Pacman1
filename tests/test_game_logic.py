import pygame
import pytest
from unittest import mock
from main import level, draw_board, draw_player, draw_misc, screen

@pytest.fixture
def mock_screen():
    pygame.init()
    screen = pygame.display.set_mode((900, 650))
    return screen

def test_level_structure():
    assert isinstance(level, list)
    assert all(isinstance(row, list) for row in level)
    assert all(isinstance(cell, int) for row in level for cell in row)

def test_draw_board_draws_all_tiles(monkeypatch):
    mock_blit = mock.MagicMock()
    monkeypatch.setattr(pygame.Surface, "blit", mock_blit)

    draw_board()

    tile_count = sum(cell != 0 for row in level for cell in row)
    assert mock_blit.call_count == tile_count

def test_tile_size_is_correct():
    assert isinstance(tile_size, int)
    assert tile_size > 0

@mock.patch("main.screen.blit")
def test_draw_player_blits_player_image(mock_blit):
    draw_player()
    assert mock_blit.called

@mock.patch("main.screen.blit")
def test_draw_misc_blits_misc_images(mock_blit):
    draw_misc()
    assert mock_blit.call_count > 0  # принаймні щось має намалювати

def test_player_position_within_bounds():
    from main import player_pos
    x, y = player_pos
    assert 0 <= x < 900
    assert 0 <= y < 650
