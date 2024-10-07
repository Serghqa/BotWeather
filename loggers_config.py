LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'default',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '__main__': {
            'handlers': ['default'],
            'formatter': 'default',
            'level': 'INFO',
            'propagate': False
        },
        'handlers.user_handlers': {
            'handlers': ['default'],
            'formatter': 'default',
            'level': 'INFO',
            'propagate': False
        },
        'functions.services': {
            'handlers': ['default'],
            'formatter': 'default',
            'level': 'INFO',
            'propagate': False
        }
    },
    'root': {
        'hadlers': ['default'],
        'level': 'INFO'
    }
}
