# Serov Sergei *28*

## Users and Groups
1. In this exercise you may need to use root privileges. You should use the sudo command whenever it’s necessary.
2. Add two users:
    1. User adduser to add user1
    ```bash
    moonlight@ubuntu:~/bynet_teach/L2$ sudo useradd -m user1
    moonlight@ubuntu:~/bynet_teach/L2$
    ```
    2. User useradd to add user2 
    ```bash
    moonlight@ubuntu:~/bynet_teach/L2$ sudo useradd -m -s /bin/bash user2
    moonlight@ubuntu:~/bynet_teach/L2$
    ```
3. Create a password for both users using the passwd command
    ```bash
    moonlight@ubuntu:~/bynet_teach/L2$ sudo passwd user1
    New password:
    Retype new password:
    passwd: password updated successfully
    moonlight@ubuntu:~/bynet_teach/L2$
    moonlight@ubuntu:~/bynet_teach/L2$ sudo passwd user2
    New password:
    Retype new password:
    passwd: password updated successfully
    moonlight@ubuntu:~/bynet_teach/L2$
    ```
4. Make sure you can switch to these users using
    1. **su** command
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ su user1
    Password:
    $ bash
    user1@ubuntu:/home/moonlight/bynet_teach/L2$ ll
    total 8
    drwxrwxr-x 2 moonlight moonlight 4096 Aug  9 21:49 ./
    drwxrwxr-x 4 moonlight moonlight 4096 Aug  9 21:49 ../
    user1@ubuntu:/home/moonlight/bynet_teach/L2$ whoami
    user1
    user1@ubuntu:/home/moonlight/bynet_teach/L2$
    ```
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ su user2
    Password:
    user2@ubuntu:/home/moonlight/bynet_teach/L2$ whoami
    user2
    user2@ubuntu:/home/moonlight/bynet_teach/L2$
    ```
    2. **sudo su** command
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ sudo su user1
    $ bash
    user1@ubuntu:/home/moonlight/bynet_teach/L2$ ll
    total 8
    drwxrwxr-x 2 moonlight moonlight 4096 Aug  9 21:49 ./
    drwxrwxr-x 4 moonlight moonlight 4096 Aug  9 21:49 ../
    user1@ubuntu:/home/moonlight/bynet_teach/L2$ whoami
    user1
    user1@ubuntu:/home/moonlight/bynet_teach/L2$
    ```
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ sudo su user2
    user2@ubuntu:/home/moonlight/bynet_teach/L2$ whoami
    user2
    user2@ubuntu:/home/moonlight/bynet_teach/L2$
    ```
    3. remember that other users do not have the ability to use sudo, so they will be required to enter their password
   ``` bash
    user1@ubuntu:/home/moonlight$ su moonlight
    Password:                                   #wrote moonlight's password
    moonlight@ubuntu:~$ exit
    exit
    user1@ubuntu:/home/moonlight$ exit
    moonlight@ubuntu:~$
   ```
5. Adding **sudo** privileges:
    * Add **user1** to the **group sudo**. Then switch to it and make sure you can use any sudo commands when you’re logged to that user.
    ``` bash
    moonlight@ubuntu:~$ sudo usermod -aG sudo user1
    moonlight@ubuntu:~$ sudo su user1
    user1@ubuntu:/home/moonlight$ sudo apt upgrade
    [sudo] password for user1:
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    Calculating upgrade... Done
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
    user1@ubuntu:/home/moonlight$
    ```
    * Sometimes we want a user to run tasks without having to enter the password each time. Make **user1** so that it doesn’t ask for password when running sudo commands.
    ``` bash
    sudo visudo
    ~~~
    @includedir /etc/sudoers.d
    moonlight ALL=(ALL) NOPASSWD:ALL

    user1 ALL=(ALL) NOPASSWD:ALL        #added this row
    ```
    * You can use **whoami** and **id** commands to verify which user you are currently logged into your current terminal, but also notice that the **prompt** changes accordingly to reflect which **username** and **hostname** you are currently logged into.
        ``` bash
        #main user moonlight
        moonlight@ubuntu:~$ id
        uid=1000(moonlight) gid=1000(moonlight) groups=1000(moonlight),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),121(lpadmin),132(lxd),133(sambashare),998(docker)

        #created user user1
        `user1`@ubuntu:/home/moonlight$ id
        uid=1001(user1) gid=1001(user1) groups=1001(user1),27(sudo)

        #created user user2
        `user2`@ubuntu:/home/moonlight$ id
        uid=1002(user2) gid=1002(user2) groups=1002(user2)
        ```
    * When you use **su** or **su –** you actually start a new **bash** inside your current **bash**. To go back one level up you can either use **exit** command, or press **ctrl+d**. Try that.
        ``` bash
        user2@ubuntu:/home/moonlight$
        user2@ubuntu:/home/moonlight$ exit
        exit
        moonlight@ubuntu:~$
        moonlight@ubuntu:~$
        ```
    * Add the ability for **user2** to run only the **id** command using **sudo**. You may have to do a little research on the syntax of /etc/sudoers file. We need add this row to file `sudo visudo`:
    ``` bash
    ...
    user2 localhost=/usr/bin/id
    ...
    ```
    ``` bash
    moonlight@ubuntu:~$ sudo visudo
    moonlight@ubuntu:~$ sudo su user2
    user2@ubuntu:/home/moonlight$ sudo less /etc/apache2/conf-available/javascript-common.conf
    [sudo] password for user2:
    user2 is not allowed to run sudo on ubuntu.  This incident will be reported.
    user2@ubuntu:/home/moonlight$
    ```
    * Lock **user2** and then try to **su** into it
    ``` bash
    moonlight@ubuntu:~$ sudo usermod -L user2
    moonlight@ubuntu:~$ su user2
    Password:
    su: Authentication failure          #user is locked
    moonlight@ubuntu:~$ sudo usermod -U user2
    moonlight@ubuntu:~$ su user2
    Password:
    user2@ubuntu:/home/moonlight$ whoami
    user2
    user2@ubuntu:/home/moonlight$
    ```
    * Delete **user2**
    ``` bash
    moonlight@ubuntu:~$ sudo userdel user2
    moonlight@ubuntu:~$
    ---
    moonlight@ubuntu:~$ cat /etc/passwd | grep user
    ...
    user1:x:1001:1001::/home/user1:/bin/bash
    user3:x:1003:1003::/home/user3:/bin/bash
    ...
    ```



---
## File ownership and permissions
1. Create a file named **hello.txt** which contains the word **“hello”**
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ echo "hello" > hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$ cat hello.txt
    hello
    moonlight@ubuntu:~/bynet_teach/L2$ 
    ```
2. Give it permissions to be run by your user
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ ls -l
    total 4
    -rw-rw-r-- 1 moonlight moonlight 6 Aug 10 18:14 hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$ chmod +x hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$ ls -l
    total 4
    -rwxrwxr-x 1 moonlight moonlight 6 Aug 10 18:14 hello.txt
    ```
3. Change the group of the file to be root (you may need sudo)
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ ls -l
    total 4
    -rw-rw-r-- 1 moonlight moonlight 6 Aug 10 18:14 hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$ sudo chgrp root hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$ ls -l
    total 4
    -rw-rw-r-- 1 moonlight root 6 Aug 10 18:14 hello.txt
    moonlight@ubuntu:~/bynet_teach/L2$
    ```
4. Perform t
    * Create hard link to that file named **hello-hard-link.txt**
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ ln hello.txt hello-hard-link.txt
    moonlight@ubuntu:~/bynet_teach/L2$ ll
    total 16
    drwxrwxr-x 2 moonlight moonlight 4096 Aug 10 18:33 ./
    drwxrwxr-x 4 moonlight moonlight 4096 Aug  9 21:49 ../
    -rw-rw-r-- 2 moonlight root         6 Aug 10 18:14 hello-hard-link.txt
    -rw-rw-r-- 2 moonlight root         6 Aug 10 18:14 hello.txt
    ```
    * Verify that both files are using the same **i-node** (hint: i-nodes)
    ``` bash
    moonlight@ubuntu:~/bynet_teach/L2$ ls -li hello*
    262181 -rw-rw-r-- 2 moonlight root       6 Aug 10 18:14 hello-hard-link.txt
    262181 -rw-rw-r-- 2 moonlight root       6 Aug 10 18:14 hello.txt
    ```
    * Create a soft-link to the file **hello-soft-link.txt**
    ``` console
    moonlight@ubuntu:~/bynet_teach/L2$ ln -s soft-to-soft-link.txt hello-soft-link.txt
    moonlight@ubuntu:~/bynet_teach/L2$ ll hello*
    -rw-rw-r-- 2 moonlight root       6 Aug 10 18:14 hello-hard-link.txt
    lrwxrwxrwx 1 moonlight moonlight 21 Aug 11 08:08 hello-soft-link.txt -> soft-to-soft-link.txt
    -rw-rw-r-- 2 moonlight root       6 Aug 10 18:14 hello.txt
    ```
5. Try to create a soft-link to a directory. Now try to create a hard-link to a directory. Did it work? Try to search the web as to why.
    ``` console
    moonlight@ubuntu:~/bynet_teach/L2$ mkdir dir-for-link
    moonlight@ubuntu:~/bynet_teach/L2$ ln -s /home/moonlight/bynet_teach/L2/dir-for-link ~/bynet_teach/L2/link
    moonlight@ubuntu:~/bynet_teach/L2$ ln /home/moonlight/bynet_teach/L2/dir-for-link ~/bynet_teach/L2/hard-link
    ln: /home/moonlight/bynet_teach/L2/dir-for-link: hard link not allowed for directory
    moonlight@ubuntu:~/bynet_teach/L2$
    ```
    ## Because 
    *   *They allow you to create loops* 
        ``` console
        mkdir -p /tmp/a/b
        cd /tmp/a/b
        ln -d /tmp/a l

        cd /tmp/a/b/l/b/l/b/l/b/l/b #Bad result
        ```
    * *They multiply files*
        ``` console
        /tmp/a/b/foo.txt
        /tmp/a/b/l/b/foo.txt #Too Bad result
        ```



---
## Packages

1. Install **apache2** package using **apt** without being asked questions (search for the appropriate flag of the apt command)
    ``` bash
    moonlight@ubuntu:~$ sudo apt install -y apache2
    Reading package lists... Done
    Building dependency tree... Done
    ...
    The following NEW packages will be installed:
    apache2 apache2-bin apache2-data apache2-utils libapr1 libaprutil1 libaprutil1-dbd-sqlite3 libaprutil1-ldap liblua5.3-0
    0 upgraded, 9 newly installed, 0 to remove and 79 not upgraded.
    ```

---
## Services
1. Use **systemctl** command to check status, stop, start, and restart the cron service
   ## status
    ``` console
    moonlight@ubuntu:~$ sudo systemctl status cron.service
    ● cron.service - Regular background program processing daemon
        Loaded: loaded (/lib/systemd/system/cron.service; enabled; vendor preset: enabled)
        Active: active (running) since Wed 2022-08-10 17:37:26 IDT; 23h ago
    ```
   ## stop
    ``` console
    moonlight@ubuntu:~$ sudo systemctl stop cron.service
    moonlight@ubuntu:~$ sudo systemctl status cron.service
    ○ cron.service - Regular background program processing daemon
        Loaded: loaded (/lib/systemd/system/cron.service; enabled; vendor preset: enabled)
        Active: inactive (dead) since Thu 2022-08-11 17:21:49 IDT; 2s ago
    ```
   ## start
    ``` console
    moonlight@ubuntu:~$ sudo systemctl status cron.service
    ● cron.service - Regular background program processing daemon
        Loaded: loaded (/lib/systemd/system/cron.service; enabled; vendor preset: enabled)
        Active: active (running) since Thu 2022-08-11 17:22:25 IDT; 3s ago
    ```
   ## restart
    ``` console
    moonlight@ubuntu:~$ sudo systemctl restart cron.service
    moonlight@ubuntu:~$ sudo systemctl status cron.service
    ● cron.service - Regular background program processing daemon
        Loaded: loaded (/lib/systemd/system/cron.service; enabled; vendor preset: enabled)
        Active: active (running) since Thu 2022-08-11 17:22:50 IDT; 2s ago
    ```
