from ask_sdk_local_debug.local_debugger_invoker import LocalDebuggerInvoker

if __name__ == "__main__":
    LocalDebuggerInvoker([
        '--accessToken', '2:TZsLh3B9ti7vpPQ5xbqNHwiJCJt90_FixzgzB8mZ1Trau0dRREHjBunPth0cXQJK:3XEXEtAXBA-kh_b1xG8Seg==',
        '--skillId', 'amzn1.ask.skill.cb2476b1-d8fd-494b-b659-cdcabcd7ce63',
        '--skillHandler', 'lambda_handler',
        '--skillFilePath', 'lambda_function.py',
        '--region', 'arn:aws:lambda:us-east-1:598628761688:function:cb2476b1-d8fd-494b-b659-cdcabcd7ce63:Release_0'
        ]
    ).invoke()