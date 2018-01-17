import sys
import subprocess
import json


def execute_local_command(command):
    try:
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True)
        # print("running local command: %s" % command)
        output = ""
        while True:
            out = process.stdout.read(1)
            if out == '' and process.poll() is not None:
                break
            if out != '':
                output += out
                sys.stdout.write(out)
                sys.stdout.flush()

        err_output = ""
        while True:
            err_out = process.stderr.read(1)
            if err_out == '' and process.poll() is not None:
                break
            if err_out != '':
                err_output += err_out
                sys.stderr.write(err_out)
                sys.stderr.flush()

        success = (process.returncode == 0)

        return success, output, err_output
    except Exception, e:
        raise e


def rds():
    end_index = 5
    # end_index = 1
    count_a = 0
    count_b = 0
    count_b_c = 0

    for i in xrange(1, end_index+1):
        command = 'aliyuncli rds DescribeDBInstances --PageSize 100 --PageNumber %s' % i
        ret_dict = json.loads(execute_local_command(command)[1])
        for ins in ret_dict['Items']['DBInstance']:
            if ins['ZoneId'] == 'cn-shanghai-MAZ1(b,c)':
                count_b_c += 1
            elif ins['ZoneId'] == 'cn-shanghai-a':
                count_a += 1
            elif ins['ZoneId'] == 'cn-shanghai-b':
                count_b += 1
            with open('result.txt', 'a') as f:
                f.write('%s,%s\n' % (ins['DBInstanceId'], ins['ZoneId']))
    print '%s, %s, %s' % (count_a, count_b, count_b_c)


if __name__ == '__main__':
    rds()

