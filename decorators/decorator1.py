from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        a = []
        for arg in args:
            a.append(str(arg))
        for k, arg in kwargs.items():
            a.append(f"{k}={arg}")
        arguments = ', '.join(a)

        with open('../main.log', 'a', encoding='utf-8') as logfile:
            logfile.write(" ======== ".join([
                str(date_time),
                func_name,
                arguments,
                str(result),
            ]))
            logfile.write('\n')

        return result

    return new_function