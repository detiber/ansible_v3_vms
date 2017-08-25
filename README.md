# ansible_v3_vms
##Create Cluster
###Basic Usage with cluster id of test
```
ansible-playbook bootstrap.yml -e kvm_snapshot_cluster_id=test -K
ansible-playbook -i inventory/cluster-test/hosts openshift-ansible/playbooks/byo/openshift-cluster/config.yml

```
###Variables
| variable                 | default                      | description |
|--------------------------|------------------------------|-------------|
| kvm_snapshot_cluster_id  | None                         | Unique cluster id (required) |
| kvm_snapshot_base_os     | rhel7                        | Base OS to build cluster on (rhel7, centos7, fedora25, fedora26) |
| kvm_snapshot_base_arch   | "{{ ansible_architecture }}" | Guest VM Arch to use for cluster |


##Tear Down Cluster
```
ansible-playbook teardown.yml -e kvm_snapshot_cluster_id=test -K
```
