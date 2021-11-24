import datetime
GAME_LOG_FILE = 'game_log.txt'

# create log string for the game start
def create_log_startstring(gamesession: int, users: dict) -> str:
    now = datetime.datetime.now()
    startstring = f'{gamesession}. Started at: {now.isoformat()}. Players: {", ".join(users.keys())}.'
    return startstring


# save game log string to file
def log_game(log_starstring: str, result: str):
    now = datetime.datetime.now()
    string = f'{log_starstring} Ended at: {now.isoformat()}. Results: {result}. \n'
    try:
        logfile = open(GAME_LOG_FILE, "a")
        logfile.write(string)
    except FileNotFoundError:
        logfile = open(GAME_LOG_FILE, "x")
        logfile.write(string)
    finally:
        logfile.close()



def get_session_number() -> int:
    """ read session number from the last line if log file exists
    if no - session number = 1 """
    try:
        with open(GAME_LOG_FILE) as logfile:
            try:
                lastline = list(logfile)[-1]
                session = int(lastline[0])
                return session + 1
            except (ValueError, IndexError):
                return 1
    except FileNotFoundError:
        return 1

