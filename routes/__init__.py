import routes.find_handle
import routes.find_by_handle
import routes.get_lsx
import routes.get_txt

ROUTER_PAIRS = {
    '/findHandle': {
        'function_name': 'find_handle',
        'description': 'Find handles in localization file(s). Case-sensitive is FALSE by default',
        'router': routes.find_handle.router
    },
    '/findByHandle': {
        'function_name': 'find_by_handle',
        'description': 'Find related files (map keys) by handle, only works for item names / descriptions',
        'router': routes.find_by_handle.router
    },
    '/getLsx': {
        'function_name': 'get_lsx',
        'description': 'Find lsx file of given map key',
        'router': routes.get_lsx.router
    },
    '/getTxt': {
        'function_name': 'get_txt',
        'description': 'Find related txt files of given map key',
        'router': routes.get_txt.router
    }
}