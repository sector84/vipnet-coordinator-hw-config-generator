import glog as log
from globals import general_params, convert_mask_to_str


def write_cfg(data, cfg_name):
    log.info(f"cfg::write_cfg : write data({data}) to file: {cfg_name} - start")
    # 1 read template
    with open(general_params.template_file_path, 'r', encoding='utf-8') as tmpl:
        content = tmpl.readlines()
    # 2 add data-specific rows
    ip_address = f"{data['bond0.100-b1']}.{data['bond0.100-b2']}.{data['bond0.100-b3']}.{data['bond0.100-b4']}"
    ip_mask = convert_mask_to_str(data['bond0.100-mask'])
    content.append(f"inet ifconfig bond0.100 address {ip_address} netmask {ip_mask}\n")

    ip_address = f"{data['bond0.101-b1']}.{data['bond0.101-b2']}.{data['bond0.101-b3']}.{data['bond0.101-b4']}"
    ip_mask = convert_mask_to_str(data['bond0.101-mask'])
    content.append(f"inet ifconfig bond0.101 address {ip_address} netmask {ip_mask}\n")

    ip_address = f"{data['bond0.102-b1']}.{data['bond0.102-b2']}.{data['bond0.102-b3']}.{data['bond0.102-b4']}"
    ip_mask = convert_mask_to_str(data['bond0.102-mask'])
    content.append(f"inet ifconfig bond0.102 address {ip_address} netmask {ip_mask}\n")

    ip_address = f"{data['eth3-p3-isp2-c2-b1']}.{data['eth3-p3-isp2-c2-b2']}.{data['eth3-p3-isp2-c2-b3']}.{data['eth3-p3-isp2-c2-b4']}"
    ip_mask = convert_mask_to_str(data['eth3-p3-isp2-c2-mask'])
    content.append(f"inet ifconfig eth3 address {ip_address} netmask {ip_mask}\n")

    with open(f'./_output/{cfg_name}', 'w', encoding='utf-8') as cfg_file:
        cfg_file.writelines(content)

    log.info(f"cfg::write_cfg : write data({data}) to file: {cfg_name} - done")
