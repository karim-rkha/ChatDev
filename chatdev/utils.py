import html
import logging
import re
import time

import markdown
import inspect
from camel.messages.system_messages import SystemMessage
from online_log.app import send_msg
import slack_sdk

def now():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def log_and_print_online(role, content=None):
    slack_token_ceo = "xoxb-6087093726343-6087843501655-ZWQwrCYjC82LarCjsmuPDwkI"  # Make sure to replace this with your actual token.
    client_ceo = slack_sdk.WebClient(token=slack_token_ceo)

    slack_token_cto = "xoxb-6087093726343-6097609059383-BLyXhPdfCtb4RdqzCB3kbx0F"  # Make sure to replace this with your actual token.
    client_cto = slack_sdk.WebClient(token=slack_token_cto)

    slack_token_cpo = "xoxb-6087093726343-6105519107398-ucfhMdJeK4XMynDYZNV0OUzy"  # Make sure to replace this with your actual token.
    client_cpo = slack_sdk.WebClient(token=slack_token_cpo)

    slack_token_prog = "xoxb-6087093726343-6135232696304-xCERMlUC0B1y5qK9qvh2KXSY"  # Make sure to replace this with your actual token.
    client_prog = slack_sdk.WebClient(token=slack_token_prog)
    
    slack_token_rev = "xoxb-6087093726343-6105608301798-ziDlbVSDqR8wCfeH67xZn6fB"  # Make sure to replace this with your actual token.
    client_rev = slack_sdk.WebClient(token=slack_token_rev)
    
    if not content:
        logging.info(role + "\n")
        send_msg("System", role)
        # Optionally, you can also send to slack here.
    else:
        print(str(role)+"\n")
        # print(str(content)+"\n")

        if role == "Chief Executive Officer":
            # If you only want to print to console.
            print(str(role)+"\n")
            print(str(content)+"\n")
            client_ceo.chat_postMessage(channel="#ping_pong_game", text=f"{content}")
        
        if role == "Chief Technology Officer":
            # If you only want to print to console.
            print(str(role)+"\n")
            print(str(content)+"\n")
            client_cto.chat_postMessage(channel="#ping_pong_game", text=f"{content}")

        if role == "Chief Product Officer":
            # If you only want to print to console.
            print(str(role)+"\n")
            print(str(content)+"\n")
            client_cpo.chat_postMessage(channel="#ping_pong_game", text=f"{content}")

        if role == "Programmer":
            # If you only want to print to console.
            print(str(role)+"\n")
            print(str(content)+"\n")
            client_prog.chat_postMessage(channel="#ping_pong_game", text=f"{content}")

        if role == "Code Reviewer":
            # If you only want to print to console.
            print(str(role)+"\n")
            print(str(content)+"\n")
            client_rev.chat_postMessage(channel="#ping_pong_game", text=f"{content}")

        logging.info(str(role) + ": " + str(content) + "\n")
        
        if isinstance(content, SystemMessage):
            records_kv = []
            content.meta_dict["content"] = content.content
            for key in content.meta_dict:
                value = content.meta_dict[key]
                value = str(value)
                value = html.unescape(value)
                value = markdown.markdown(value)
                value = re.sub(r'<[^>]*>', '', value)
                value = value.replace("\n", " ")
                records_kv.append([key, value])
            content = "**[SystemMessage**]\n\n" + convert_to_markdown_table(records_kv)
        else:
            role = str(role)
            content = str(content)

        send_msg(role, content)



def convert_to_markdown_table(records_kv):
    # Create the Markdown table header
    header = "| Parameter | Value |\n| --- | --- |"

    # Create the Markdown table rows
    rows = [f"| **{key}** | {value} |" for (key, value) in records_kv]

    # Combine the header and rows to form the final Markdown table
    markdown_table = header + "\n" + '\n'.join(rows)

    return markdown_table


def log_arguments(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        params = sig.parameters

        all_args = {}
        all_args.update({name: value for name, value in zip(params.keys(), args)})
        all_args.update(kwargs)

        records_kv = []
        for name, value in all_args.items():
            if name in ["self", "chat_env", "task_type"]:
                continue
            value = str(value)
            value = html.unescape(value)
            value = markdown.markdown(value)
            value = re.sub(r'<[^>]*>', '', value)
            value = value.replace("\n", " ")
            records_kv.append([name, value])
        records = f"**[{func.__name__}]**\n\n" + convert_to_markdown_table(records_kv)
        log_and_print_online("System", records)

        return func(*args, **kwargs)

    return wrapper
