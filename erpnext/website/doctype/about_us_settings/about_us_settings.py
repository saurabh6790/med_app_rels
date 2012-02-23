# ERPNext - web based ERP (http://erpnext.com)
# Copyright (C) 2012 Web Notes Technologies Pvt Ltd
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
generate html
"""
import webnotes

class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl
		
	def on_update(self):
		"""make home html"""
		from website.utils import make_template
		import os
		path = os.path.join(os.path.dirname(__file__), 'template.html')
		
		self.doc.about_team = webnotes.conn.sql("""select * from `tabAbout Us Team` 
			where parent='About Us Settings' order by idx""", as_dict=1)
		
		import markdown2
		for t in self.doc.about_team:
			t['bio'] = markdown2.markdown(t.get('bio') or '')
		
		webnotes.conn.set_value('Page', 'about', 'title', self.doc.headline)
		webnotes.conn.set_value('Page', 'about', 'content', make_template(self.doc, path))
