"""Run the migrator tool through its CLI."""
from pathlib import Path
import sys
from migrator import cli

if __name__ == '__main__':
    config_path = Path(Path(__file__).parent.resolve(), '..', '..', '..', 'config')
    config_path = config_path.resolve() if config_path.exists() else None

    print("debug")
    print(sys.argv)
    print(config_path)
    print(sys.argv[1:])
    
    cli.run(sys.argv[1:], config_path)
