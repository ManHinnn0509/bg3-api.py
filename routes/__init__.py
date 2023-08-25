import routes.find_handle
import routes.find_by_handle

ROUTER_PAIRS = {
    '/findHandle': {
        'function_name': 'find_handle',
        'description': 'Find handles in localization file(s)',
        'router': routes.find_handle.router
    },
    '/findByHandle': {
        'function_name': 'find_by_handle',
        'description': 'Find related files by handle',
        'router': routes.find_by_handle.router
    }
}