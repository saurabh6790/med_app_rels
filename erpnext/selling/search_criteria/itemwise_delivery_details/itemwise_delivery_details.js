// ERPNext - web based ERP (http://erpnext.com)
// Copyright (C) 2012 Web Notes Technologies Pvt Ltd
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

report.customize_filters = function() {
  this.filter_fields_dict['Delivery Note'+FILTER_SEP +'From Voucher Date'].df['report_default'] = sys_defaults.year_start_date;
  this.filter_fields_dict['Delivery Note'+FILTER_SEP +'To Voucher Date'].df['report_default'] = dateutil.obj_to_str(new Date());
  this.filter_fields_dict['Delivery Note'+FILTER_SEP +'From Posting Date'].df['report_default'] = sys_defaults.year_start_date;
  this.filter_fields_dict['Delivery Note'+FILTER_SEP +'To Posting Date'].df['report_default'] = dateutil.obj_to_str(new Date());

}