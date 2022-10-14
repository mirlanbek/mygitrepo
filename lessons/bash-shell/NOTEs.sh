

--------------------------------------
/usr/bin/tail -F -n0 ./virt-install.log &
tailpid=$!
./start.sh

kill $tailpid
--------------
su - root -c /opt/manage.sh
-----

nmcli con (down, up, show) add type ethernet con-name eth0 ifname eth0 (dhcp till here) ipv4.address 192.168.1.112/24 ipv4.method static


# ---------------------- id -u ---- id -g -----------------------

chown $(id -u):$(id -g) $HOME/.kube/config

# ------------------------ vitualization --------------

#from epel:
yum install msr-tools -y
rdmsr 0x3a

#if output 3 or 5  means virtualization enabled
# -------------- New scripting ------------------------------------------------

if [[ $1 == *","* ]]; then
    IFS=',' read -r -a srcs <<< "$1"
    if [[ ${#srcs[@]} -lt 2 ]]; then
        echo "Number of sources read in as list: ${#srcs[@]}
              Need at least two values to take a csv list as
              argument. Error fatal: exiting."
        exit 1
    fi
else
    srcs="$1"
fi

for src in ${srcs[@]}; do
    if [ $("$getent_path" group "$src") ] ; then
        src_str=$("$getent_path" group "$src" | cut -d ':' -f 4)
        IFS=',' read -r -a src_usrs <<< $src_str
        for usr in ${src_usrs[@]}; do
            "$usermod_path" -a -G  "$dest" "$usr"
        done
    else
        echo "Source group $src does not exist.
              Trying next group."
    fi
done


# -----------------------------------------------------------------------------------------

docker save openvino | gzip > openvino.tar.gz


# ------------------------- Samba ----------------------------------------------------------
# pdbedit -L ; smbpasswd -a root ; systemctl start nmb smb;


[linux]
path=/root/samba
write list = root

# ---------------------------- Vagrantfile-virtualbox--------------------------------------------

# -*- mode: ruby -*-
# vi: set ft=ruby :

$vm_number = 3

Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu1804"
    config.vm.network :public_network,
      :dev => "virbr0",
      :mode => "bridge",
      :type => "bridge"

    config.vm.provider :virtualbox do |virtualbox|
    end

    (0..$vm_number-1).each do |i|
        config.vm.define vm_name = "server%d" % i do |vsmc|

            vsmc.vm.hostname = vm_name

            vsmc.vm.provider :virtualbox do |domain|
              domain.memory = 2048
              domain.cpus = 2
            end
        end
    end
end

# ------------------------ Vagrantfile libvirt --------------------------------------------------

# Note: if cannot restart start libvirt-bin, no probs, just install virt-manager and vagrant up.

# -*- mode: ruby -*-
# vi: set ft=ruby :

$vm_number = 2

Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu1804"
    config.vm.network :public_network,
      :dev => "virbr0",
      :mode => "bridge",
      :type => "bridge"

    config.vm.provider :libvirt do |libvirt|
        libvirt.driver = "kvm"
        libvirt.username = "root"
        libvirt.storage_pool_name = "default"
    end

    (0..$vm_number-1).each do |i|
        config.vm.define vm_name = "vsmc%d" % i do |vsmc|
            vsmc.vm.hostname = vm_name

            vsmc.vm.provider :libvirt do |domain|
              domain.memory = 1028
              domain.cpus = 1
            end
        end
    end
end

#----------- Create centos iso and *.vmdk VM image  ----------------------------------------------------

1. Download net Centos iso
 wget -O install.iso http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/images/boot.iso


2. Make live image:  (create "build/liveimage.img")

/usr/bin/tail -F -n0 ./virt-install.log &
tailpid=$!

then
     if [ -z "${https_proxy}" ]; then
     sudo livemedia-creator --nomacboot --project BullSequanaSA-tools \
        --release 64.01 --make-iso --image-only --resultdir ./build \
        --iso=./install.iso --ks=./rhel-minimal.ks \
        --image-name liveimage.img \
        --anaconda-arg="--product CentOS Linux" \
        --dracut-arg="--xz" \
        --dracut-arg="--no-hostonly" \
        --dracut-arg="--debug" \
        --dracut-arg="--no-early-microcode" \
        --dracut-arg="--omit plymouth" \
        --dracut-arg="--add livenet dmsquash-live convertfs pollcdrom qemu qemu-net" \
        --dracut-arg="--add-drivers mptbase mptscsih mptspi hv_storvsc hid_hyperv hv_netvsc hv_vmbus" 
/usr/bin/kill $tailpid        
     # track progress during legacy image creation

3. mv build/liveimage.img . && rm -rf build

4.  MAKE LIVE CD out of liveimage.img
        mkdir /tmp/livecd

     #  mount liveimage.img to /tmp/livecd
        sudo mount -o loop,offset=1048576 liveimage.img /tmp/livecd

# Creating Toolbox image
        ./toolbox-create-script.sh


5. copy all tools to mounted "liveimage.img":

        sudo cp -vf BullSequanaSA-tools.tar /tmp/livecd/usr/share/
        sudo cp -vf load-image.sh /tmp/livecd/usr/bin/
        # These scripts cause the OS to install the container on boot.
        sudo cp -vf image-build-scripts/instcont.sh /tmp/livecd/opt/instcont.sh
        sudo cp -vf image-build-scripts/instcont /tmp/livecd/etc/cron.d/

6. umount and remove /tmp/livecd/
sudo umount /tmp/livecd
rm -rf /tmp/livecd


7. Boot VM to activate container image
sudo qemu-img create -f qcow2 -b ./liveimage.img -F raw snapshot.img
export LIBGUESTFS_BACKEND=direct
sudo virt-install -n buildvm --description "Boot build image" --ram=8096 --vcpus=2 --disk path=./snapshot.img --import

 8. Sparsify and convert image to raw format.
virt-sparsify snapshot.img --format qcow2 --convert raw liveos.img

9. Delete the buildvm
sudo virsh undefine --nvram buildvm

10. # Export as OVA
virt-sparsify --format raw --convert vmdk -o adapter_type=lsilogic,subformat=streamOptimized,compat6 ./ovaimage.img ./BSAController.vmdk
tar -czvf BSAController.ova BSAController.ovf BSAController.vmdk
rm -rf build
----------------------------------------------------------------------------------------------


