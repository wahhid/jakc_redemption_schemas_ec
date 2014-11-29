from openerp.osv import fields, osv
from datetime import datetime

AVAILABLE_STATES = [
    ('draft','Draft'),
    ('waiting','Waiting'),
    ('review','Review'),
    ('open','Open'),                        
    ('done','Close'),    
]

AVAILABLE_BLAST_STATES = [
    ('draft','Draft'),
    ('ready','Ready'),
    ('process','Process'),                        
    ('done','Close'),    
    ('failed','Failed'),
]

AVAILABLE_EMAIL_STATES = [
    ('draft','Draft'),
    ('ready','Ready'),
    ('sent','Sent'),                        
    ('failed','Failed'),
]

AVAILABLE_TYPE_STATES = [
    ('email','Email'),
    ('sms','SMS'),
]


AVAILABLE_SEARCH_TYPE_STATES = [
    ('all','All'),
    ('customer','By Customer'),
    ('zone','By Zone'),    
]


class rdm_schemas_segment(osv.osv):
    _name = 'rdm.schemas.segment'
    _description = 'Redemption Trans Segment'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','Schemas', readonly=True),
        'age_segment': fields.many2one('rdm.age.segment','Age Segment'),
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_segment()   

class rdm_schemas_gender(osv.osv):
    _name = 'rdm.schemas.gender'
    _description = 'Redemption Schemas gender'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','Schemas', readonly=True),
        'gender_id': fields.many2one('rdm.customer.gender','Gender'),        
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_gender()


class rdm_schemas_ayc_participant(osv.osv):
    _name = 'rdm.schemas.ayc.participant'
    _description = 'Redemption Trans AYC Participant'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','Schemas', readonly=True),
        'participant_id': fields.selection([('1','AYC non participant tenant'),('2','AYC participant tenant')],'Participant Type',required=True),
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_ayc_participant()   


class rdm_schemas_religion(osv.osv):
    _name = 'rdm.schemas.religion'
    _description = 'Redemption Schemas Religion'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','Schemas', readonly=True),
        'religion_id': fields.many2one('rdm.customer.religion','Religion'),        
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_religion()

class rdm_schemas_ethnic(osv.osv):
    _name = 'rdm.schemas.ethnic'
    _description = 'Redemption Schemas Ethnic'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','Schemas', readonly=True),
        'ethnic_id': fields.many2one('rdm.customer.ethnic','Ethnic'),
    }   
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_ethnic()   

class rdm_schemas_tenant(osv.osv):
    _name = 'rdm.schemas.tenant'
    _description = 'Redemption schemas Tenant'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'tenant_id': fields.many2one('rdm.tenant','Tenant'),
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_tenant()   

class rdm_schemas_marital(osv.osv):
    _name = 'rdm.schemas.marital'
    _description = 'Redemption schemas Marital'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'marital_id': fields.many2one('rdm.customer.marital','Marital'),
    }   
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_marital()   

class rdm_schemas_interest(osv.osv):
    _name = 'rdm.schemas.interest'
    _description = 'Redemption schemas Interest'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'interest_id': fields.many2one('rdm.customer.interest','Interest'),
    }    
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_interest()   

class rdm_schemas_card_type(osv.osv):
    _name = 'rdm.schemas.card.type'
    _description = 'Redemption schemas Card Type'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'card_type_id': fields.many2one('rdm.card.type','Card Type'),
    }   
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_card_type()   

class rdm_schemas_tenant_category(osv.osv):
    _name = 'rdm.schemas.tenant.category'
    _description = 'Redemption schemas Tenant Category'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'tenant_category_id': fields.many2one('rdm.tenant.category','Tenant Category'),
    }   
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_tenant_category()   

class rdm_schemas_rules(osv.osv):
    _name = 'rdm.schemas.rules'
    _description = 'Redemption schemas Rules'
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas','schemas', readonly=True),
        'rules_id': fields.many2one('rdm.rules','Rules'),
        'schemas': fields.selection([('ditotal','Di Total'),('terbesar','Terbesar')],'Schemas'),
    }   
    _defaults = {
        'schemas_id': lambda self, cr, uid, context: context.get('schemas_id', False),}
        
rdm_schemas_rules()   

class rdm_schemas_blast(osv.osv):
    _name = 'rdm.schemas.blast'
    _description = 'Redemption Schemas Blast'
    
    def _get_trans(self, cr, uid, trans_id, context=None):
        return self.browse(cr, uid, trans_id, context=context)
    
    def start_blast(self, cr, uid, ids, context=None):
        trans_id = ids[0]
        trans = self._get_trans(cr, uid, trans_id, context)
    
    def blast_customer(self, cr, uid, ids, context=None):
        return {
               'type': 'ir.actions.act_window',
               'name': 'Blast Customer',
               'view_mode': 'form',
               'view_type': 'form',                              
               'res_model': 'rdm.schemas.blast.customer',
               'nodestroy': True,
               'target':'new',
               'context': {'blast_customer_id': ids[0]},
        } 
            
    _columns = {
        'schemas_id': fields.many2one('rdm.schemas', 'Schemas', readonly=True),
        'schedule': fields.datetime('Schedule',required=True),        
        'type': fields.selection(AVAILABLE_TYPE_STATES,'Type', size=16, required=True),
        'blast_detail_ids': fields.one2many('rdm.schemas.blast.detail','blast_id', readonly=True),
        'state': fields.selection(AVAILABLE_BLAST_STATES, 'Status', size=16, readonly=True),
    }
    _defaults = {
        'state': lambda *a: 'draft',
    }
rdm_schemas_blast()

class rdm_schemas_blast_detail(osv.osv):
    _name = 'rdm.schemas.blast.detail'
    _description = 'Redemption Schemas Blast Detail'
    _columns = {
        'blast_id': fields.many2one('rdm.schemas.blast', 'Schemas Blast', readonly=True),
        'customer_id': fields.many2one('rdm.customer', 'Customer', required=True),
        'state': fields.selection(AVAILABLE_EMAIL_STATES, 'Status', size=16, readonly=True)
    }
    _defaults = {
        'state': lambda *a: 'draft',
    }
rdm_schemas_blast_detail()

class rdm_schemas_blast_customer(osv.osv_memory):
    _name = 'rdm.schemas.blast.customer'
    _description = 'Redemption Schema Blast Customer'
    
    def add_customer(self, cr, uid, ids, context=None):
        params = self.browse(cr, uid, ids, context=context)
        param = params[0]           
        customer_id = context.get('blast_customer_id',False)
        data = {}              
        if param.password_new == param.password_confirm:
            data.update({'password':param.password_new})
            self.pool.get('rdm.customer').write(cr, uid, [customer_id], data, context=context)                                                
        return True
        
    _columns = {
        'search_type': fields.selection(AVAILABLE_SEARCH_TYPE_STATES,'Search Type', size=16, required=True),
        'search_by_customer': fields.many2one('rdm.customer','Customer'),
        'search_by_zone': fields.many2one('rdm.customer.zone','Customer Zone'),        
    }
    
class rdm_schemas(osv.osv):
    _name = 'rdm.schemas'
    _description = 'Redemption schemas'
        
    def schemas_review(self, cr, uid, ids, context=None):        
        self.write(cr,uid,ids,{'state':'review'})
        #Send Email To Manager  
        return True
    
    def schemas_start(self, cr, uid, ids, context=None):      
        if self._get_open_schemas(cr, uid, ids,context):
            raise osv.except_osv(('Warning'), ('There are active schemas'))
        else:
            self.write(cr,uid,ids,{'state':'open'})  
            return True
   
    def schemas_close(self, cr, uid, ids, context=None):        
        self.write(cr,uid,ids,{'state':'done'})  
        return True

    def schemas_reset(self, cr, uid, ids, context=None):        
        self.write(cr,uid,ids,{'state':'open'})  
        return True
    
    def schemas_waiting(self, cr, uid, ids, context=None):        
        self.write(cr,uid,ids,{'state':'waiting'})  
        return True
    
    def _get_trans(self, cr, uid, ids , context=None):
        trans_id = ids[0]
        return self.browse(cr, uid, trans_id, context=context);
        
    def _get_open_schemas(self, cr, uid, trans_id, context=None):        
        trans = self._get_trans(cr, uid, trans_id, context)     
        ids = None   
        if trans.type == 'promo':
            ids = self.pool.get('rdm.schemas').search(cr, uid, [('type','=','promo'),('state','=','open'),], context=context)
        if trans.type == 'point':
            ids = self.pool.get('rdm.schemas').search(cr, uid, [('type','=','point'),('state','=','open'),], context=context)            
        if ids:
            return True
        else:
            return False        

    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'type': fields.selection([('promo','Promo'),('point','Point')],'Type',readonly=True),        
        'description': fields.text('Description',required=True),
        'desc_email': fields.text('Description For Email',required=True),
        'desc_sms': fields.char('Description For SMS', size=140,required=True),
        'start_date': fields.date('Start Date',required=True),
        'end_date': fields.date('End Date',required=True),
        'last_redeem': fields.date('Last Redeem',required=True),                
        'draw_date': fields.date('Draw Date',required=True),
        'spend_amount': fields.float('Spend Amount',required=True),
        'coupon': fields.integer('Coupon #',required=True),
        'point': fields.integer('Point #',required=True),        
        'limit_point': fields.integer('Point Limit',help="-1 for No Limit",required=True),
        'point_expired_date': fields.date('Point Expired Date', required=True),
        'segment_ids': fields.one2many('rdm.schemas.segment','schemas_id','Segment'),
        'image1': fields.binary("schemas Image"),
        
        #Customer Filter
        'gender_ids': fields.one2many('rdm.schemas.gender','schemas_id','schemas Gender'),
        'religion_ids': fields.one2many('rdm.schemas.religion','schemas_id','schemas Religion'),
        'ethnic_ids': fields.one2many('rdm.schemas.ethnic','schemas_id','schemas Ethnic'),
        'tenant_ids': fields.one2many('rdm.schemas.tenant','schemas_id','schemas Tenant'),
        'marital_ids': fields.one2many('rdm.schemas.marital','schemas_id','schemas Marital'),
        'interest_ids': fields.one2many('rdm.schemas.interest','schemas_id','schemas Interest'),
        'card_type_ids': fields.one2many('rdm.schemas.card.type','schemas_id','schemas AYC Card Type'),  
        
        #Tenant Filter          
        'tenant_category_ids': fields.one2many('rdm.schemas.tenant.category','schemas_id','Tenant Category'),
        'ayc_participant_ids': fields.one2many('rdm.schemas.ayc.participant','schemas_id','AYC Participant'),
        
        #Bank Filter
        
        #Rules List        
        'rules_ids': fields.one2many('rdm.schemas.rules','schemas_id','Rules'),        
        
        #Blast List
        'blast_ids': fields.one2many('rdm.schemas.blast','schemas_id','Blast'),
        
        'receipt_header': fields.char('Receipt Header', size=50),
        'receipt_footer': fields.text('Receipt Footer'),
        'state':  fields.selection(AVAILABLE_STATES, 'Status', size=16, readonly=True),
    }
        
    _defaults = {
        'state': lambda *a: 'draft',
        'draw_date': fields.date.context_today,
        'coupon': lambda *a: 0,
        'limit_point': lambda *a: -1,
    }
        
    def create(self, cr, uid, values, context=None):                            
        id =  super(rdm_schemas, self).create(cr, uid, values, context=context)
        self.schemas_waiting(cr, uid, [id], context)
        return id    

rdm_schemas()
