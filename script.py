import subprocess

def configure_dom0_memory(memory):
    """
    Configuration de le memoire pour le Dom0
    """
    cmd = ["xl", "info"]
    output = subprocess.check_output(cmd).decode("utf-8")
    lines = output.split('\n')
    for line in lines:
        if line.startswith("total_memory"):
            total_memory_kb = int(line.split(':')[1].strip())
            total_memory_mb = total_memory_kb / 1024
            break
    
    dom0_memory_mb = memory
    if dom0_memory_mb > total_memory_mb:
        print("Erreur: La mémoire Dom0 ne peut pas dépasser la mémoire totale")
        return False
    
    cmd = ["xl", "mem-set", "0", "{}M".format(dom0_memory_mb)]
    subprocess.run(cmd)
    print("Mémoire Dom0 configurée sur {} MB".format(dom0_memory_mb))
    return True

def configure_dom0_vcpus(vcpus):
    """
    Configuration du vCPUs pour le Dom0
    """
    cmd = ["xl", "vcpu-set", "0", str(vcpus)]
    subprocess.run(cmd)
    print("Dom0 vCPUs configured to {}".format(vcpus))

if __name__ == "__main__":
    # Configuration des paramètres
    dom0_memory_mb = 4096  # Exemple: 4GB
    dom0_vcpus = 4  # Exemple: 4 vCPUs

    # Configuration memoire Dom0
    if configure_dom0_memory(dom0_memory_mb):
        # Configuration vCPUs Dom0
        configure_dom0_vcpus(dom0_vcpus)
    else:
        print("Échec de la configuration de la mémoire Dom0. Sortir.")
