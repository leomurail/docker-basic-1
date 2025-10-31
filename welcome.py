import datetime
import platform
import os

def banner() -> str:
    return (
        f"Bonjour {os.getenv("WELCOME_NAME", "Docker")} ! \n"
        f"Date et heure : {datetime.datetime.utcnow().isoformat()}Z\n"
        f"Système : {platform.system()} {platform.release()}"
    )

if __name__ == "__main__":
    print(banner())
