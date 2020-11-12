from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', '<ACCESS_TOKEN>',
        '--skillId', '<SKILL_ID>',
        '--skillHandler', '<HANDLER_NAME>',
        '--skillFilePath', '<FILE_NAME>']
    ).invoke()