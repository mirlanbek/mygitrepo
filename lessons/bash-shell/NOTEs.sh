
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

#---------------------------------------------------------------