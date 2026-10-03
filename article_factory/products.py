from __future__ import annotations


PRODUCT_BY_GAME = {
    "dota2": "Melonity",
    "cs2": "cluster.center",
    "deadlock": "cluster.center",
}


def product_for_game(game: str | None) -> str:
    if not game or game == "all":
        return "the mapped product"
    return PRODUCT_BY_GAME.get(game.lower(), "the mapped product")
