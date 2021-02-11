import asyncio

from pysplunk import splunk


async def main():
    try:
        print('configuring...')
        splunk.configure_logger(
            'my_app', '1.0.1', 'test', 'DEBUG')
        print('logdebug...')
        await splunk.logdebug(
            'account', 'workflow type', 'workflow instance', '"logdebug"',
            {'custom1': 'test'}, "evidence")
        print('loginfo...')
        await splunk.loginfo(
            'account', 'workflow type', 'workflow instance', 'loginfo',
            evidence="evid info")
        print('logwarn...')
        await splunk.logwarn(
            'account', 'workflow type', 'workflow instance', 'logwarn',
            evidence="evid warn")
        i = 1 / 0
    except Exception as ex:
        print('logerror...')
        await splunk.logerror(
            'account', 'workflow type', 'workflow instance', 'logerror',
            {'custom1': 'test'}, ex)


if __name__ == '__main__':
    print('testing...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('end!')
