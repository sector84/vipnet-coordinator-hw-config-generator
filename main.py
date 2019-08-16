import argparse
import glog as log
from globals import general_params

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--verbosity", type=int, default=10, help="""logging verbosity level (by default DEBUG (10)):
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
""")
ap.add_argument("-f", "--file", required=True, help="path to the input xlsx file to generate configs to")
ap.add_argument("-t", "--template", required=True, help="path to the template to use to generate config files")

args = vars(ap.parse_args())
log.setLevel(args['verbosity'])
log.info("Logs initialized successfully.")

general_params.load_params(args)
log.info("General params initialized successfully.")


def main():
    log.info("main")
    from xls import get_config_data
    from config import write_cfg
    for row in get_config_data():
        write_cfg(row, f"{row['hostname']}.txt")
    log.info('main -> done')


if __name__ == "__main__":
    main()
