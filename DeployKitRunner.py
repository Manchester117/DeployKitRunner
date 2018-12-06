from ActionExec.ActionWrapper import deploy_server_run
from DisplayMenu.IsLocalCompile import display_is_local_compile
from DisplayMenu.IsPullCode import display_is_pull_code
from DisplayMenu.SelectMachine import display_server_menu
from DisplayMenu.SelectProject import display_project_menu
from LoadSetting.LoadSetting import get_config_element


def work_flow_dispatcher():
    pull_code_param = get_config_element('PullCodeTask')                # 从TFS上将代码拉取到本地
    display_is_pull_code(pull_code_param)

    compile_code_param = get_config_element('CompileTask')              # 本地编译代码
    display_is_local_compile(compile_code_param)

    deploy_param = get_config_element('DeployTask')                     # 通过用户选择获取要发布的服务器和对应站点/服务
    deploy_server_list = display_server_menu(deploy_param)

    all_deploy_list = display_project_menu(deploy_server_list)          # 这里把发布单独提出来
    deploy_server_run(all_deploy_list)


if __name__ == '__main__':
    work_flow_dispatcher()