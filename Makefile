install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

brain-even:
	uv run --active brain-even

brain-calc:
	uv run --active brain-calc

brain-gcd:
	uv run --active brain-gcd

brain-progression:
	uv run --active brain-progression

brain-prime:
	uv run --active brain-prime