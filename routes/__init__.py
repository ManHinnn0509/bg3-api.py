import routes.find_handle
import routes.find_by_handle
import routes.get_lsx

ROUTER_PAIRS = {
    '/findHandle': {
        'function_name': 'find_handle',
        'description': 'Find handles in localization file(s)',
        'router': routes.find_handle.router
    },
    '/findByHandle': {
        'function_name': 'find_by_handle',
        'description': 'Find related files by handle, only works for item names / descriptions',
        'router': routes.find_by_handle.router
    },
    '/getLsx': {
        'function_name': 'get_lsx',
        'description': 'Find related files using map key',
        'router': routes.get_lsx.router
    }
}