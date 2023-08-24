import routes.find_handle

ROUTER_PAIRS = {
    '/findHandle': {
        'description': 'Find handles in localization file(s)',
        'router': routes.find_handle.router
    }
}