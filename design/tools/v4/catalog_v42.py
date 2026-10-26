"""v4.2 catalog section: Control Tower, inbox and Order 360 parts. Idempotent (replaces its own block)."""
import pathlib, re, json
ROOT = pathlib.Path(__file__).resolve().parents[2]
CAT = ROOT / 'system' / 'components' / 'catalog.html'
REG = ROOT / 'system' / 'components' / 'registry.json'
MAP = ROOT / 'system' / 'maps' / 'opc-shadcn.json'
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
sign = lambda k, i, t: f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(i)}</span>{t}</span>'
st = lambda k, s, t, w, d='', x='': (f'<li class="c-timeline__item c-timeline__item--{k}"><span class="c-timeline__time">{t}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
                                     f'<span class="c-timeline__body"><span class="c-timeline__src">{s}</span><span class="c-timeline__what">{w}</span>'
                                     + (f'<span class="c-timeline__who">{d}</span>' if d else '') + f'{x}</span></li>')

BLOCK = f'''<!-- v42:start -->
  <section class="sec" aria-labelledby="s-v42-work">
    <h2 id="s-v42-work">Control Tower · c-works / c-work · r-tower</h2>
    <p>Mỗi việc OPC theo dõi: trạng thái (chữ + hình), giờ, tiêu đề, một dòng tình hình, nguồn. Việc đang mở có nền biển nhạt. Trang dùng r-tower: danh sách | chi tiết (≥1024), điện thoại mở chi tiết thành trang riêng.</p>
    <div class="surface demo-col"><ul class="c-works">
      <li><a class="c-work" href="#" aria-current="true"><span class="c-work__state">{sign('you','i-alert','Cần chị quyết')}</span><span class="c-work__when">09:03</span><span class="c-work__t">Đơn Sunrise Hotel · 20 gói bò, 30 hũ muối</span><span class="c-work__m">Dừng vì khách nợ quá hạn 12 ngày</span><span class="c-work__src">Zalo OA · Trợ lý đọc tin</span></a></li>
      <li><a class="c-work" href="#"><span class="c-work__state">{sign('wait','i-clock','Đang chạy')}</span><span class="c-work__when">07:30</span><span class="c-work__t">Chế biến 40 gói bò một nắng</span><span class="c-work__m">Đang sấy · xong khoảng 16:00</span><span class="c-work__src">Lệnh LCB-0412</span></a></li>
      <li><a class="c-work" href="#"><span class="c-work__state">{sign('err','i-alert','Lỗi')}</span><span class="c-work__when">10:12</span><span class="c-work__t">Hoá đơn DH-2047</span><span class="c-work__m">Chưa rõ đã phát hành · OPC hỏi lại lúc 11:15</span><span class="c-work__src">Kết nối X Invoice</span></a></li>
    </ul></div>
  </section>

  <section class="sec" aria-labelledby="s-v42-story">
    <h2 id="s-v42-story">Câu chuyện của một việc · c-timeline__src (--ai · --ok · --now · --err · --next) · c-rules · c-decide</h2>
    <p>Mỗi bước nói ai làm: Trợ lý đề xuất · OPC kiểm tra · Chị duyệt · Kết nối. Bước chưa xảy ra nhạt bằng màu, không bằng độ mờ. Khung quyết định: vấn đề, tác động (số lớn), đề xuất, lý do bắt buộc (để trống, có gợi ý), ai được duyệt.</p>
    <div class="surface demo-col"><ol class="c-timeline">
      {st('ai','Trợ lý đề xuất','09:02','Đọc tin của chị Mai (Sunrise Hotel)','20 gói bò · 30 hũ muối · giao trước 15:00 mai')}
      {st('ok','OPC kiểm tra','09:02','Giá · tồn · công nợ','', '<ul class="c-rules" aria-label="Kết quả kiểm tra"><li class="c-rules__r">'+ic('i-check')+'Giá</li><li class="c-rules__r">'+ic('i-check')+'Tồn</li><li class="c-rules__r c-rules__r--fail">'+ic('i-x')+'Công nợ</li></ul>')}
      {st('now','Chờ chị duyệt','Bây giờ','Đơn dừng lại — chưa giữ hàng','', '<div class="c-decide"><p class="c-decide__q">Duyệt đơn dù khách đang nợ quá hạn?</p><dl class="c-kv"><dt>Tác động</dt><dd><b class="c-decide__fig">14.650.000 ₫</b> công nợ sau đơn này</dd></dl><label class="c-field"><span class="c-field__label">Lý do của chị (bắt buộc)</span><span class="c-field__control"><input class="c-field__input" id="cat-rs" placeholder="Ví dụ: khách quen, hẹn trả khi nhận hàng"></span></label><div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">Duyệt đơn</button><button class="c-btn" type="button">Từ chối</button></div></div>')}
      {st('err','Kết nối · X Invoice','10:12','Không trả lời sau 30 giây','OPC không tự gửi lại')}
      {st('next','Sau khi chị duyệt','','OPC kiểm tra lại → giữ hàng')}
    </ol>
    <p class="c-decide__auto">{ic('i-clock')}OPC không tự gửi lại · đang tự hỏi lại, lần sau 11:15</p>
    <div class="c-decide__acts"><button class="c-btn" type="button" aria-disabled="true">{ic('i-lock')}Phát hành lại</button></div></div>
  </section>

  <section class="sec" aria-labelledby="s-v42-quote">
    <h2 id="s-v42-quote">Yêu cầu bán · c-quote · c-match (--unsure)</h2>
    <p>Tin gốc giữ nguyên như khách gửi (chữ, ảnh, ghi âm, file); chỗ Trợ lý chưa chắc được tô. Mỗi dòng: khách viết gì → khớp món nào.</p>
    <div class="surface demo-col"><figure class="c-quote"><figcaption class="c-quote__from"><b>Ảnh đơn viết tay</b> chị An chụp lúc 10:40</figcaption>
      <div class="c-quote__media">{ic('i-photo')}<span>“Gió Núi — bò 1 nắng 10 gói, muối kiến <mark>1? 7?</mark> hũ”</span></div></figure>
      <p class="c-match"><b>“bò 1 nắng 10 gói”</b><small>Khớp: Bò một nắng 500g</small></p>
      <p class="c-match c-match--unsure"><b>“muối kiến 1? 7? hũ”</b><small>Chưa rõ: 1 hay 7 hũ</small></p></div>
  </section>

  <section class="sec" aria-labelledby="s-v42-journey">
    <h2 id="s-v42-journey">Order 360 · c-journey (--done · --now · --warn)</h2>
    <p>Một đơn đang ở đâu trong cả vòng đời. Chặng hiện tại màu biển, chặng xong biển nhạt; điện thoại xếp 3 cột.</p>
    <div class="surface demo-col"><ol class="c-journey" aria-label="Đơn đang ở đâu">
      <li class="c-journey__s c-journey__s--done">Nhận yêu cầu</li><li class="c-journey__s c-journey__s--done">Kiểm tra</li><li class="c-journey__s c-journey__s--done">Chị duyệt</li>
      <li class="c-journey__s c-journey__s--done">Giữ hàng</li><li class="c-journey__s c-journey__s--now" aria-current="step">Soạn</li><li class="c-journey__s">Giao</li>
      <li class="c-journey__s">Hoá đơn</li><li class="c-journey__s c-journey__s--warn">Tiền</li><li class="c-journey__s">Đóng đơn</li></ol></div>
  </section>
<!-- v42:end -->
'''

s = CAT.read_text()
s = re.sub(r'<!-- v42:start -->.*?<!-- v42:end -->\n', '', s, flags=re.S)
s = s.replace('\n</main>', '\n' + BLOCK + '</main>', 1)
need = {'i-alert', 'i-clock', 'i-check', 'i-x', 'i-photo', 'i-lock'}
have = set(re.findall(r'<symbol id="(i-[a-z-]+)"', s))
icons = {**json.load(open(ROOT / 'system/assets/icons/lucide-map.json')), **json.load(open(ROOT / 'system/assets/icons/lucide-extra.json'))}
add = ''.join(f'<symbol id="{i}" viewBox="0 0 24 24">{icons[i]}</symbol>' for i in sorted(need - have) if i in icons)
if add:
    s = s.replace('</svg>', add + '</svg>', 1)
CAT.write_text(s)

r = json.load(open(REG))
r.update({
 'c-works': {"name": "WorkList", "apg": None, "role": "list of links", "variants": [], "parts": ["c-work"], "shadcn": "custom", "since": "4.2.0"},
 'c-work': {"name": "WorkItem", "apg": None, "role": "link", "variants": ["aria-current"], "parts": ["state", "when", "t", "m", "src"], "shadcn": "custom", "since": "4.2.0", "note": "one tracked job (Control Tower) or one sales request"},
 'r-tower': {"name": "ListDetailSplit", "apg": None, "role": "two regions", "variants": ["--list (phone: list only)"], "parts": ["detail", "k", "t"], "shadcn": "custom", "since": "4.2.0"},
 'c-rules': {"name": "RuleChecks", "apg": None, "role": "list", "variants": ["__r--fail"], "parts": ["r"], "shadcn": "Badge list", "since": "4.2.0"},
 'c-decide': {"name": "DecisionPanel", "apg": "group", "role": "group", "variants": [], "parts": ["q", "fig", "acts", "who", "auto"], "shadcn": "custom (Card + Field + Button)", "since": "4.2.0", "note": "reason field empty with a placeholder; risky paths aria-disabled until confirmed"},
 'c-quote': {"name": "SourceQuote", "apg": None, "role": "figure", "variants": [], "parts": ["from", "text", "media"], "shadcn": "custom", "since": "4.2.0"},
 'c-match': {"name": "MatchLine", "apg": None, "role": "text", "variants": ["--unsure"], "parts": [], "shadcn": "custom", "since": "4.2.0"},
 'c-journey': {"name": "OrderJourney", "apg": None, "role": "list (aria-current=step)", "variants": ["__s--done", "__s--now", "__s--warn"], "parts": ["s"], "shadcn": "custom", "since": "4.2.0"},
})
json.dump(r, open(REG, 'w'), ensure_ascii=False, indent=2)
m = json.load(open(MAP))
for n in ['WorkList', 'WorkItem', 'ListDetailSplit', 'RuleChecks', 'DecisionPanel', 'SourceQuote', 'MatchLine', 'OrderJourney']:
    m['components'].setdefault(n, {"use": f"custom shared component src/components/opc/{n}.tsx", "custom": True})
json.dump(m, open(MAP, 'w'), ensure_ascii=False, indent=2)
print('catalog v4.2 + registry + map')
