from FUtils import write_txt,write_html
from Config import G_REPORT_HEAD,G_DEV_SIZE
import pyshark
from FCheckers import dump_url
from tqdm import tqdm

def load_flow(filename,filter=None,isDev=None):
    traffic_data = []
    print("target file: %s ..." % filename)
    if filter:
        print("shark filter: %s"%filter)
        cap = pyshark.FileCapture(filename, keep_packets=False,display_filter=filter)
    else:
        cap = pyshark.FileCapture(filename, keep_packets=False)

    print("start anayse ...")
    if isDev:
        count = 0
        for packet in tqdm(cap, desc="Loading packets"):
            traffic_data.append(packet)
            count += 1
            if count > G_DEV_SIZE:
                break
    else:
        for packet in tqdm(cap, desc="Loading packets"):
            traffic_data.append(packet)
    print("total packets: %d"%len(traffic_data))
    return traffic_data

def analyse(filename,filter,checkers,scanbin=None,isDev=None):
    # 数据预加载
    traffic_data = load_flow(filename,filter=filter,isDev=isDev)
    # 生成报告头
    report_text = G_REPORT_HEAD % (filename, filter,len(traffic_data))
    # # binwalk文件分析
    # if scanbin:
    #     report_text += binscan(filename)
    # 启动包检查
    text_report = check_loop(filename,traffic_data,checkers,report_text)
    # 输出报告
    write_txt("report.md",text_report)
    write_html("report.html",text_report)
    #write_html2("report2.html",text_report)

def dump_by_url(filename,url):
    traffic_data = load_flow(filename,filter="http")
    url_list = []
    print("start dump urls ...")
    for packet in tqdm(traffic_data, total=len(traffic_data), desc="check packets"):
        tmp_result = dump_url.check_byurl(packet,url)
        if tmp_result:
            url_list.append(tmp_result)
    print("got %d urls."%len(url_list))
    print("save urls file in dump_url.csv.")
    dump_url.report(url_list,"dump_url.csv")

def dump_by_keyword(filename,key):
    traffic_data = load_flow(filename,filter="http")
    url_list = []
    print("start dump urls, key is %s"%key)
    for packet in tqdm(traffic_data, total=len(traffic_data), desc="check packets"):
        tmp_result = dump_url.check_bykey(packet,key)
        if tmp_result:
            url_list.append(tmp_result)
    print("got %d urls."%len(url_list))
    print("save urls file in dump_url.csv.")
    dump_url.report(url_list,"dump_url.csv")

def dump_by_keylen(filename,pkt_length):
    traffic_data = load_flow(filename,filter="http")
    url_list = []
    print("start dump urls ...")
    for packet in tqdm(traffic_data, desc="check packets"):
        tmp_result = dump_url.check_bylen(packet,pkt_length)
        if tmp_result:
            url_list.append(tmp_result)
    print("got %d urls."%len(url_list))
    print("save urls file in dump_url.csv.")
    dump_url.report(url_list,"dump_url.csv")


def check_loop(filename,traffic_data,checkors,report_head):
    tmp_data = {}
    report_text = ""+report_head
    # 数据初始化
    for checkor in checkors:
        tmp_data[checkor.name] = []
    # 数据包分析
    for packet in tqdm(traffic_data, total=len(traffic_data), desc="check packets"):
    #for packet in traffic_data:
        for checkor in checkors:
            tmp_result = checkor.check(packet)
            if tmp_result:
                tmp_data[checkor.name].append(tmp_result)

    # 报告整理
    for checkor in checkors:
        tmp_report = checkor.report(tmp_data[checkor.name])
        report_text += tmp_report
    report_text += "\n\n\n\n"
    return report_text
