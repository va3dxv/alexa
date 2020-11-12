from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', '<ACCESS_TOKEN>',
        '--skillId', 'amzn1.ask.skill.b5c3a293-cf6d-43aa-b94d-ffb55c6ddf7a',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', 'lambda_function.py',
        '--region', 'NA(North America)'
        ]
    ).invoke()