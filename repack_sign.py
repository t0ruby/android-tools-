import os
import click

JKS_PATH = './sources/sign.jks'
JKS_ALIAS = 'sign'
JKS_PASS = '123456'


@click.command()
@click.option('-i', prompt='unsigned apk', help='unsigned apk path')
@click.option('-o', prompt='signed apk', help='signed apk path')
@click.option('-j', default=JKS_PATH, help='jks path, default sign.jks')
@click.option('-a', default=JKS_ALIAS, help='jks alias, default sign')
@click.option('-p', default=JKS_PASS, help='jks password, default 123456')
def sign(i: str, o: str, j: str, a: str, p: str):
    # jarsigner -verbose -keystore ../../sign.jks -signedjar ./app-debug-release.apk ./app-debug.apk sign
    os.system(f'jarsigner -verbose -keystore {j} -storepass {p} -signedjar {o} {i} {a}')


if __name__ == '__main__':
    sign()
