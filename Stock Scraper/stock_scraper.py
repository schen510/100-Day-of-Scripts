import sys
import jarvis.crawler as crawler


def main():
    if len(sys.argv) < 2:
        print "ERROR - Not enough command line arguments provided." + \
        "\nUsage: python stock_scraper.py CMD" +                      \
        "\nCMD - display | add | remove " +                           \
        "\ndisplay" +                                                 \
        "\t\t- accesses the database and displays everything" +       \
        "\nadd" +                                                     \
        "\t\t- adds a new stock ticker into the database" +           \
        "\nremove" +                                                  \
        "\t\t- removes a stock ticker from the database"


if __name__ == "__main__":
    main()