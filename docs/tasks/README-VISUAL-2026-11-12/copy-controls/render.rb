require 'rdoc'
require 'rdoc/markdown'
require 'rdoc/markup/to_html'
require 'fileutils'
require 'cgi'
root=Dir.pwd
parser=RDoc::Markdown.new
convert=->(text){ RDoc::Markup::ToHtml.new(RDoc::Options.new).convert(parser.parse(text)) }
lines=File.readlines('README.md'); result=''; buffer=''; i=0
flush=-> { result << convert.call(buffer) unless buffer.empty?; buffer='' }
while i<lines.length
 line=lines[i]
 if line.start_with?('|')
  flush.call; rows=[]
  while i<lines.length && lines[i].start_with?('|')
   rows << lines[i].strip.split('|', -1)[1...-1].map(&:strip);i+=1
  end
  result << '<table><thead><tr>'+rows.first.map{|c|'<th>'+convert.call(c).gsub(%r{</?p>},'').strip+'</th>'}.join+'</tr></thead><tbody>'
  rows.drop(2).each{|r|result << '<tr>'+r.map{|c|'<td>'+convert.call(c).gsub(%r{</?p>},'').strip+'</td>'}.join+'</tr>'}
  result << '</tbody></table>'; next
 elsif line.match?(%r{^</?(div|details|summary)}) || line.start_with?('<img ')
  flush.call; result << line
 else
  buffer << line
 end
 i+=1
end
flush.call
result.gsub!(%r{<h([1-6]) id="[^"]*">(.*?)<span>.*?</span></h\1>}m){level=$1;label=$2;id=CGI.unescapeHTML(label).downcase.gsub(/<[^>]+>/,'').gsub(/[^a-z0-9\s-]/,'').gsub(/\s+/,'-');"<h#{level} id=\"#{id}\">#{label}</h#{level}>"}
css=<<~CSS
*{box-sizing:border-box}html{color-scheme:light dark}body{margin:0;background:#f6f8fa;color:#1f2328;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:1100px;margin:32px auto;padding:40px 48px;background:#fff;border:1px solid #d1d9e0;border-radius:8px}h1{font-size:44px;margin:6px 0 12px;letter-spacing:-1px}h2{font-size:24px;line-height:1.3;margin:30px 0 16px;border-bottom:1px solid #d1d9e0;padding-bottom:8px}h3{font-size:20px;margin:16px 0}p{margin:0 0 16px}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}img{max-width:100%;height:auto}hr{border:0;border-top:1px solid #d1d9e0;margin:28px 0}ul,ol{padding-left:28px;margin:0 0 16px}li p{margin:0}li+li{margin-top:5px}table{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto;margin:16px 0}td,th{border:1px solid #d1d9e0;padding:8px 12px;text-align:left}tr:nth-child(2n){background:#f6f8fa}pre{padding:16px;background:#f6f8fa;overflow:auto;border-radius:6px;font-size:13px;line-height:1.5}code{font-family:ui-monospace,monospace}details{border:1px solid #d1d9e0;border-radius:6px;padding:12px 16px;margin:12px 0}summary{cursor:pointer}details[open] summary{margin-bottom:12px}.preview-note{max-width:1100px;margin:16px auto -16px;color:#59636e;font-size:12px;padding:0 16px}body.dark{background:#0d1117;color:#e6edf3}body.dark main{background:#0d1117;border-color:#30363d}body.dark a{color:#58a6ff}body.dark h2,body.dark td,body.dark th,body.dark details,body.dark hr{border-color:#30363d}body.dark pre,body.dark tr:nth-child(2n){background:#161b22}body.dark .preview-note{color:#8b949e}@media(max-width:600px){main{margin:0;padding:24px 16px;border:0;border-radius:0}h1{font-size:36px}h3{font-size:18px}body{font-size:15px}.preview-note{margin:8px 0}table{font-size:13px}}
CSS
html='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Agent Kit — README preview</title><style>'+css+'</style><link rel="stylesheet" href="copy.css"><body><p class="preview-note">Bản xem trước cục bộ từ README.md · Bố cục mô phỏng GitHub; chưa xác minh trên GitHub.</p><main>'+result+'</main><script src="copy.js"></script></body></html>'
File.write('/tmp/agent-kit-readme-preview/index.html',html)
FileUtils.mkdir_p('/tmp/agent-kit-readme-preview/docs/assets')
FileUtils.cp(Dir['docs/assets/*.svg'],'/tmp/agent-kit-readme-preview/docs/assets')
puts "Rendered local preview: headings=#{result.scan('<h2').length}, tables=#{result.scan('<table').length}, prompts=#{result.scan('<pre>').length}, details=#{result.scan('<details>').length}"
