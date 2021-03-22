import os

print("This program will enable ping to only one website as per your desire ")

site=input("Enter the website address you want to be blocked ..\n")


out = os.popen('nslookup {}'.format(site)).read().split()


os.system('route add -net {} gw 192.168.29.1 netmask 255.255.255.255  reject enp0s3'.format(out[9]))

os.system('route -n')

print('Please try to ping {}'.format(site))

print(Thankyou ..!)
