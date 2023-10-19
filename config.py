env = 'dev'

conf_dict = {
    "prod": {
        "log_level": "INFO",
        "base_url": "https://google.com"

    },
    "dev": {
        "log_level": "DEBUG",
        "base_url": "https://google.com"
    }
}
config = conf_dict[env]
