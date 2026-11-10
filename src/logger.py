import logging


class ColorFormatter(logging.Formatter):
    _colors = {
        logging.CRITICAL: "\033[91m",  # Red
        logging.ERROR: "\033[91m",  # Red
        logging.WARNING: "\033[93m",  # Yellow
        logging.INFO: "\033[92m",  # Green
        logging.DEBUG: "\033[95m",  # Magenta
    }
    _marks = {
        logging.CRITICAL: "!",
        logging.ERROR: "E",
        logging.WARNING: "W",
        logging.INFO: "*",
        logging.DEBUG: "D",
    }
    _reset = "\033[0m"
    _blue = "\033[94m"
    _bold = "\033[1m"

    def format(self, rec):
        marks, colors = self._marks, self._colors
        return (
            f"{self._blue}{self._bold}[{colors[rec.levelno]}{marks[rec.levelno]}"
            f"{self._blue}]{self._reset} {super().format(rec)}"
        )


logger = logging.getLogger("kul_app")
logger.setLevel(logging.DEBUG)

# Stream
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(ColorFormatter("[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
streamhandler.setLevel(logging.INFO)
logger.addHandler(streamhandler)

# File
file_handler = logging.FileHandler("kul_app.log")
file_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# Loki?
# Egen for error.log, egen info.log, access.log, flask_auth.log?
streamhandler.setLevel(0)
logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")
