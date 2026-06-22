from random import choice, randint


PARTS = ("la", "pa", "ga")


def generate_tortle_name(parts: int = 3) -> str:
    """Generate a tortle name using only la, pa, and ga."""
    return "".join(choice(PARTS) for _ in range(parts))


if __name__ == "__main__":
    print(generate_tortle_name(8))
