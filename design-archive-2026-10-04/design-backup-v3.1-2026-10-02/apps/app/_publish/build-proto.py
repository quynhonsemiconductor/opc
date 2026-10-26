import json, os, re, shutil
SRC = '/Users/benq/Desktop/qnsc/opc/design'
OUT = '/tmp/opc-proto'  # temporary bundle folder; publish it with the Artifact tool (root = OUT)
SHELL = SRC + '/apps/app/_publish/prototype-shell.html'
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/screens'); os.makedirs(OUT + '/system/components'); os.makedirs(OUT + '/system/assets')

man = json.load(open(SRC + '/apps/app/uiux-studio.json'))
files = {}
for f in sorted(os.listdir(SRC + '/apps/app/screens')):
    if not f.endswith('.html') or f.startswith('_'): continue
    s = open(SRC + '/apps/app/screens/' + f).read().replace('../../../system/', '../system/')
    open(OUT + '/screens/' + f, 'w').write(s); files['screens/' + f] = OUT + '/screens/' + f
for p in ['tokens.css', 'components/components.css', 'components/recipes.css', 'components/catalog.html', 'assets/qr-demo.svg']:
    shutil.copy(SRC + '/system/' + p, OUT + '/system/' + p); files['system/' + p] = OUT + '/system/' + p
shutil.copy(SRC + '/apps/app/app-tokens.css', OUT + '/app-tokens.css'); files['app-tokens.css'] = OUT + '/app-tokens.css'
m = open(SRC + '/system/directions/a-pro/motion.html').read().replace('href="tokens.css"', 'href="../system/tokens.css"').replace('href="../../components/', 'href="../system/components/').replace('<link rel="stylesheet" href="skin.css">\n', '')
open(OUT + '/screens/motion.html', 'w').write(m); files['screens/motion.html'] = OUT + '/screens/motion.html'
man['screens'].append({'file': 'motion.html', 'title': 'Chuyển động & tương tác (bấm thử)', 'status': 'review', 'states': []})

NOTES = {
 'home.html': 'Trả lời hai câu: tiền hôm nay đã thật chưa, và việc gì làm trước. Làn số 1 là việc phải làm ngay.',
 'counter.html': 'Bán tại quầy: chọn món, giỏ, thu tiền QR. Thang "ĐANG Ở ĐÂY" cho biết tiền đang ở bước nào.',
 'counter--received.html': 'Khách đã chuyển, ngân hàng chưa khớp sao kê. Giao hàng trước được vì đơn dưới mức 2.000.000 ₫.',
 'counter--verified.html': 'Tiền đã khớp sao kê MB. Hoá đơn tự phát hành và chờ mã CQT.',
 'counter--cash.html': 'Thu tiền mặt: nhập khách đưa, tiền thối hiện to và rõ.',
 'counter--offline.html': 'Mất kết nối ngân hàng: QR tạm tắt, vẫn bán bằng tiền mặt hoặc công nợ.',
 'money.html': 'Tiền theo độ chắc chắn: đã xác minh, chờ xác minh (có tuổi), chưa gán. Một việc vàng: gán khoản 2.150.000 ₫.',
 'money--assign.html': 'Gán khoản chuyển khoản không có mã đơn. Ứng viên kèm lý do khớp và không khớp; không có gì được lưu trước khi bấm.',
 'orders.html': 'Đơn hôm nay, tab theo trạng thái, tìm kiếm, chọn thời gian, lọc và sắp xếp.',
 'orders--filtered.html': 'Đang lọc: mỗi bộ lọc là một chip bỏ được; số đơn và tổng tiền hiện ngay.',
 'invoices.html': 'Hoá đơn máy tính tiền và mã CQT. Hoá đơn chờ mã vẫn hợp lệ để đưa khách.',
 'invoices--accountant.html': 'Góc nhìn kế toán: bảng dày, 25 dòng mỗi trang, hoá đơn lỗi báo ngay đầu trang.',
 'order-detail.html': 'Chi tiết đơn Zalo chờ xác nhận, kèm công nợ hiện tại của khách và lịch sử đơn.',
 'invoice-detail.html': 'Bản xem trước hoá đơn như giấy, trạng thái mã CQT và lịch sử gửi.',
 'onboard-welcome.html': 'Bắt đầu đăng ký. Khoảng 15 phút, làm dở vẫn lưu; có thể làm cùng nhân viên OPC.',
 'onboard-products--review.html': 'AI đọc bảng giá viết tay. Hai món AI chưa chắc được đưa lên đầu để chị Hai kiểm tra.',
 'onboard-help.html': 'Trợ giúp ở mọi bước: người thật trước (chị Lan, Zalo, người thân), câu trả lời tự động sau.',
 'onboard-firstsale.html': 'Bán thử có hướng dẫn, đơn bán thử không tính doanh thu.',
 'motion.html': 'Bấm thử: tiền về rồi được xác minh, thêm vào giỏ, duyệt có hoàn tác, hover, tooltip, giải thích thuật ngữ.',
 'home--assistant.html': 'Trợ lý bên cạnh: biết đang ở màn nào, trả lời kèm nguồn, mọi đề xuất phải qua Cần xử lý.',
 'home--command.html': 'Bảng lệnh ⌘K: gõ để đi tới, làm việc, tìm đơn.',
 'home--simple.html': 'Chế độ Gọn, chữ lớn cho chủ hộ: chỉ tiền hôm nay và việc cần làm.',
 'money--help.html': 'Trợ giúp ngay trên màn: 3 bước ngắn, video 30 giây, “Gọi lại cho tôi”.',
 'orders--peek.html': 'Xem nhanh đơn ở ngăn bên phải, không rời danh sách.',
 'orders--bulk.html': 'Chọn nhiều đơn, gửi nhắc nợ qua Zalo một lần; chế độ xem đã lưu.',
 'orders--bulk--preview.html': 'Trước khi gửi hàng loạt: xem người nhận, tin nhắn mẫu, cảnh báo khách có thể đã trả; có hoàn tác.',
 'settings-display.html': 'Cỡ chữ, chế độ Gọn/Đầy đủ, tương phản và chuyển động cho từng người.',
 'receipt.html': 'Phiếu in và tin Zalo khách nhận được: bộ mặt của hộ trước người mua.',
 'settings-users--otp.html': 'Việc nhạy cảm cần mã xác nhận qua Zalo; OPC không tự chuyển tiền hay nộp thuế.',
 'approvals.html': 'Việc chờ duyệt: mọi thứ Trợ lý, ngân hàng hay hệ thống soạn sẵn, kèm bằng chứng và hậu quả, chờ chủ hộ duyệt.',
 'audit.html': 'Nhật ký: ai (người, Trợ lý, hệ thống) đã làm gì, lúc nào, trước và sau. Không sửa, không xoá được.',
 'home--more.html': 'Điện thoại: mục Thêm liệt kê mọi nơi trong app, Cần xử lý đứng đầu.',
 'settings-features.html': 'Bật tắt tính năng theo từng hộ để menu luôn gọn; tính năng bắt buộc theo luật bị khoá kèm lý do.',
 'settings-users.html': 'Người dùng và quyền: chủ hộ, quản lý, thu ngân, kế toán được uỷ quyền có hạn.',
 'onboard-assisted.html': 'Màn của nhân viên hỗ trợ trên laptop: mã QR để chị Hai quét, có tạo mã mới và cách xác minh bằng giấy.',
}
GROUPS = [
 ('Đăng ký lần đầu', [f for f in ['onboard-welcome','onboard-phone','onboard-otp','onboard-otp--wrong','onboard-household','onboard-household--notfound','onboard-verify','onboard-verify--camera','onboard-verify--camera-denied','onboard-verify--failed','onboard-bank','onboard-bank--done','onboard-bank--mismatch','onboard-products','onboard-products--review','onboard-products--unreadable','onboard-help','onboard-invoice','onboard-firstsale','onboard-done','onboard-assisted']]),
 ('Tổng quan', ['home','home--loading','home--offline','home--firstrun']),
 ('Quầy bán hàng', ['counter','counter--received','counter--verified','counter--cash','counter--offline','counter--empty','counter--cart','counter--payment','counter--payment--received','counter--payment--verified']),
 ('Tiền & đối soát', ['money','money--assign']),
 ('Đơn hàng', ['orders','orders--loading','orders--search','orders--noresult','orders--filters','orders--daterange','orders--filtered','order-detail']),
 ('Hoá đơn', ['invoices','invoice-detail','invoices--accountant']),
 ('Cần xử lý', ['approvals','audit']),
 ('Lớp Pro: hỗ trợ, năng suất, tin cậy', ['motion','home--assistant','home--notifications','home--command','home--simple','money--help','orders--peek','orders--bulk','orders--bulk--preview','settings-display','receipt','settings-users--otp']),
 ('Cài đặt & điều hướng', ['home--more','settings-users','settings-features']),
]
PHONE = {'home--more','home--simple','counter--cart','counter--payment','counter--payment--received','counter--payment--verified','onboard-firstsale'} | {g for g in GROUPS[0][1] if g != 'onboard-assisted'}
screens = []
for s in man['screens']:
    f = s['file']; sid = f[:-5]
    if not os.path.exists(OUT + '/screens/' + f): continue
    t = s.get('title', sid)
    t = t.replace('Onboarding · ', '').replace('Onboarding ', 'Bước ')
    screens.append({'file': f, 'title': t, 'stateOf': s.get('stateOf'), 'note': NOTES.get(f, ''),
                    'sizes': 'phone' if sid in PHONE else ('desktop' if sid == 'onboard-assisted' else 'any')})
groups = [{'name': n, 'files': [x + '.html' for x in fs]} for n, fs in GROUPS]
listed = {x for g in groups for x in g['files']}
missing = [s['file'] for s in screens if s['file'] not in listed]
flows = [{'name': fl['name'], 'steps': [x if isinstance(x, str) else x['screen'] for x in fl['steps']]} for fl in man.get('flows', [])]
flows.insert(1, {'name': 'Khi đăng ký gặp lỗi', 'steps': ['onboard-otp--wrong.html','onboard-household--notfound.html','onboard-verify--camera-denied.html','onboard-verify--failed.html','onboard-bank--mismatch.html','onboard-products--unreadable.html','onboard-help.html']})
flows.append({'name': 'Chi tiết đơn và hoá đơn', 'steps': ['orders.html','order-detail.html','invoices.html','invoice-detail.html','invoices--accountant.html']})
DATA = {'screens': screens, 'groups': groups, 'flows': flows, 'version': man['designVersion']}
shell = open(SHELL).read().replace('/*DATA*/{}', json.dumps(DATA, ensure_ascii=False))
shell = shell.replace('thiết kế v1.5', 'thiết kế v' + man['designVersion'])
open(OUT + '/prototype.html', 'w').write(shell)
json.dump(files, open(OUT + '/_files.json', 'w'), indent=0)
print(len(files), 'files; screens', len(screens), '; not grouped:', missing)
