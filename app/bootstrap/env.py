from dotenv import load_dotenv, find_dotenv

loaded = load_dotenv(
    find_dotenv("../.env") if find_dotenv(".env") == "" else find_dotenv(".env")
)
