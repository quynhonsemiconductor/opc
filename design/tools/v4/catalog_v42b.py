"""v4.2 catalog section (delivery): r-board skinned for OPC, board card states, r-pick, c-sim, courier COD. Idempotent."""
import pathlib, re, json
ROOT = pathlib.Path(__file__).resolve().parents[2]
CAT = ROOT / 'system/components/catalog.html'; REG = ROOT / 'system/components/registry.json'; MAP = ROOT / 'system/maps/opc-shadcn.json'
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
BLOCK = f'''<!-- v42b:start -->
  <section class="sec" aria-labelledby="s-v42-board">
    <h2 id="s-v42-board">Giao hàng · r-board (skin OPC) · r-board__card (--you) · r-board__sum · c-sim</h2>
    <p>Pattern board của skill, đổi sang token OPC. Đầu cột: tên · số đơn · tiền thu hộ (luôn có chỗ). Thẻ cần chủ hộ được nâng (viền đỏ). Trạng thái mô phỏng có nhãn “Mô phỏng” riêng.</p>
    <div class="r-board" aria-label="Ví dụ bảng"><section class="r-board__col" aria-labelledby="cb1"><h3 class="r-board__head" id="cb1">Đang giao <span class="r-board__count">2</span><span class="r-board__sum">thu hộ 1.150.000 ₫</span></h3><ul class="r-board__list">
      <li><article class="r-board__card r-board__card--you" aria-labelledby="cbx"><span class="r-board__meta"><b>DH-2045</b><span>09:40</span></span><h4 class="r-board__t" id="cbx">Homestay Mây Ngàn</h4><span class="r-board__lines">6 hũ muối</span><span class="c-sign c-sign--err"><span class="c-sign__pic">{ic('i-alert')}</span>Không giao được · khách đóng cửa</span><span class="r-board__acts"><a class="c-btn" href="#">Giao lại</a></span></article></li>
      <li><article class="r-board__card" aria-labelledby="cby"><span class="r-board__meta"><b>DH-2050</b><span>hẹn mai</span></span><h4 class="r-board__t" id="cby">Anh Nam</h4><span class="r-board__how">{ic('i-link')}Đơn vị vận chuyển · GHTK</span><span class="c-sign c-sign--wait"><span class="c-sign__pic">{ic('i-clock')}</span>Đang trung chuyển</span><span class="c-sim">Mô phỏng</span></article></li>
    </ul></section></div>
  </section>
  <section class="sec" aria-labelledby="s-v42-pick">
    <h2 id="s-v42-pick">Soạn hàng · r-pick · nút chính bị khoá kèm lý do</h2>
    <div class="surface demo-col"><ul class="r-pick"><li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">{ic('i-check')}</span><span class="r-pick__name"><b>Bò một nắng 500g</b><small>Lô BMN-0405</small></span><span class="r-pick__qty"><b>20</b>/20 gói</span></li>
      <li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true"></span><span class="r-pick__name"><b>Muối kiến vàng 100g</b><small>Lô MKV-0921</small></span><span class="r-pick__qty"><b>18</b>/30 hũ</span></li></ul>
      <div class="c-decide__acts"><button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic('i-lock')}Bàn giao · còn thiếu 12 hũ</button></div></div>
  </section>
<!-- v42b:end -->
'''
s = CAT.read_text(); s = re.sub(r'<!-- v42b:start -->.*?<!-- v42b:end -->\n', '', s, flags=re.S)
s = s.replace('\n</main>', '\n' + BLOCK + '</main>', 1)
icons = {**json.load(open(ROOT / 'system/assets/icons/lucide-map.json')), **json.load(open(ROOT / 'system/assets/icons/lucide-extra.json'))}
have = set(re.findall(r'<symbol id="(i-[a-z-]+)"', s))
add = ''.join(f'<symbol id="{i}" viewBox="0 0 24 24">{icons[i]}</symbol>' for i in sorted({'i-alert', 'i-link', 'i-clock', 'i-check', 'i-lock'} - have))
if add: s = s.replace('</svg>', add + '</svg>', 1)
CAT.write_text(s)
r = json.load(open(REG))
r.update({'r-board': {"name": "Board", "apg": None, "role": "regions per stage", "variants": ["__card--you"], "parts": ["col", "head", "count", "sum", "list", "card", "t", "lines", "how", "cod", "acts", "tabs"], "shadcn": "custom (skill pattern r-board, OPC skin)", "since": "4.2.0", "note": "phone: stage tabs, one column at a time; drag is never the only way (buttons on cards)"},
          'r-pick': {"name": "PickList", "apg": None, "role": "list", "variants": ["__chk--ok"], "parts": ["l", "chk", "name", "qty"], "shadcn": "custom", "since": "4.2.0"},
          'c-sim': {"name": "SimulatedTag", "apg": None, "role": "text", "variants": [], "parts": [], "shadcn": "Badge (outline, dashed)", "since": "4.2.0"},
          'r-courier': {"name": "CourierLink", "apg": None, "role": "page (no shell)", "variants": [], "parts": ["cod", "or", "issue"], "shadcn": "custom", "since": "4.2.0"}})
json.dump(r, open(REG, 'w'), ensure_ascii=False, indent=2)
m = json.load(open(MAP))
for n in ['Board', 'PickList', 'SimulatedTag', 'CourierLink']:
    m['components'].setdefault(n, {"use": f"custom shared component src/components/opc/{n}.tsx", "custom": True})
json.dump(m, open(MAP, 'w'), ensure_ascii=False, indent=2)
print('catalog v4.2b')
