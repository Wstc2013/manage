from jwlog import models
from jumpserver.api import *
# Create your views here.

@require_role(role='user')
def jwlog_list(request):
    jwlogs = models.Log.objects.all()
    return my_render('jwlog/jwlog_list.html', locals(), request)

@require_role(role='user')
def monitor_list(request):
    file_path = request.GET.get('file_path', '')
    web_terminal_uri = '/ws/logmonitor?file_path=%s' % (file_path)
    return my_render('jwlog/jwlog_jk.html', locals(), request)

@require_role(role='user')
def monitor_hostory_list(request):
    file_path = request.GET.get('file_path', '')
    option_val = request.GET.get('option_val', '')
    monitor_cmd = '/usr/bin/tail -%s %s' % (option_val,file_path)
    monitor_status, monitor_ret = command(monitor_cmd)
    monitor_ret_list = monitor_ret.split('\n')
    if monitor_status != 0:
        logger.error('jwlog: monitor_cmd run error')
    return my_render('jwlog/jwlog_jk_history.html', locals(), request)