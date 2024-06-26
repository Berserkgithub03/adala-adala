from django.urls import path
from .views import lawyerhome,subscribe,inbox,chat,inboxnew,NotaryRegisterView,lawyer_profile,home,home2,Lawall,message_form, test, profile, RegisterView,LawyerRegisterView
from . import views
from .views import manage_clients,subscription_confirmation
from .views import lawyerhome, ninbox, notaryhome,subscribe,inbox,chat,inboxnew,NotaryRegisterView,lawyer_profile,home,home2,Lawall,message_form, test, profile, RegisterView,LawyerRegisterView

urlpatterns = [
    path('ninbox/', ninbox, name='ninbox'),
    path('unauthorized/', views.unauthorized_access, name='unauthorized_access'),
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('basetest/', views.basetest, name='basetest'), 
    path('subscription/confirmation/', subscription_confirmation, name='subscription_confirmation'),
    path('send-message/', views.send_message, name='send_message'),
    path('lawregister/', LawyerRegisterView.as_view(), name='lawregister'),
    path('notary_register/', NotaryRegisterView.as_view(), name='notary_register'),
    path('registernot/', views.register_notary, name='register_notary'),
    path('test/', test, name='test'),
    path('home2/', home2, name='home2'),
    path('lawyerhome/', lawyerhome, name='lawyerhome'),
    path('inboxnew/', inboxnew, name='inboxnew'),
    path('message_form/<int:recipient_id>/', views.message_form, name='message_form'),
    path('message_form/', views.message_form, name='message_form'),
    path('Lawall/', Lawall, name='Lawall'),
    path('Notaryall/', views.Notaryall, name='Notaryall'),
    path('search_notaries/', views.search_notaries, name='search_notaries'),
    path('chat/', chat, name='chat'),
    path('search/', views.search_lawyers, name='search_lawyers'),
    path('lawyer-profile/', lawyer_profile, name='lawyer_profile'),
    path('message_form_lawyer/<int:lawyer_id>/', message_form, name='message_form_lawyer'),
    path('message_form_recipient/<int:recipient_id>/', message_form, name='message_form_recipient'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('manage_clients/', manage_clients, name='manage_clients'),
    path('subscribe/', subscribe, name='subscribe'),
    path('inbox/', inbox, name='inbox'),
    path('conversation/<int:sender_id>/', views.conversation, name='conversation'),
    path('send-message/<int:sender_id>/', views.send_message, name='send_message'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('pclients/', views.pclients, name='pclients'), 
    path('upclient/<int:client_id>/', views.update_client, name='update_client'),

    path('affaire/', views.affairepage, name='affaire'), 
    path('delete_clients/<int:cid>/', views.delete_client, name='delete_clients'),
    path('delete_nclients/<int:cid>/', views.delete_nclient, name='delete_nclients'),
    path('delete_seance/<int:cid>/', views.delete_seance, name='delete_seance'),
    path('delete_pay/<int:cid>/', views.delete_pay, name='delete_pay'),
    path('delete_doc/<int:cid>/', views.delete_doc, name='delete_doc'),

    path('jugements/', views.jugements, name='jugements'),
    path('get_conseil_data/', views.get_conseil_data, name='get_conseil_data'),
    path('get_tribunals/', views.get_tribunals, name='get_tribunals'),
    path('tablejugement/', views.tablejugement, name='tablejugement'),
    path('printjt/', views.printjt, name='printjt'),
    path('documents/<int:Aff_id>/', views.add_document, name='add_document'),

    path('viewaffaire/<int:Aff_id>/', views.detailed_view, name='viewaffaire'),
    path('seances/<int:Aff_id>/add/', views.add_seance, name='add_seance'),
    path('seances/<int:Aff_id>/', views.detailed_view, name='seances'),
    path('PrintSeance/<int:sea_id>/', views.printseance, name='PrintSeance'),

    path('printjuge/<int:Aff_id>/', views.printjuge, name='printjuge'),
    path('delete_affaire/<int:cid>/', views.delete_affaire, name='delete_affaire'),

    path('verdict/<int:Aff_id>/', views.add_verdict, name='verdict'),
    path('paiements/<int:Aff_id>/', views.add_paiement, name='paiements'),
    path('paiementpdf/<int:pay_id>/', views.printpaiement, name='paiementpdf'),

    path('tableseances/', views.tableseances, name='tableseances'),
    path('updateseance/<int:seance_id>/', views.updateseance, name='updateseance'),

    path('todayseances/', views.todayseances, name='todayseances'),
    path('tomorowseances/', views.tomorrowseances, name='tomorowseances'),
    path('weekseances/', views.weekseances, name='weekseances'),
    path('tribunals/', views.tribunal_list, name='tribunals'),
    path('registerall/', views.registerall, name='registerall'),
    path('homesearch_results/', views.homesearch_results, name='homesearch_results'),
    path('news_list/', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('create/', views.create_news, name='create_news'),
    path('<int:pk>/update/', views.update_news, name='update_news'),
    path('<int:pk>/delete/', views.delete_news, name='delete_news'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('Clients/', views.display_clients, name='Clients'), 
    path('uprdv/<int:rdv_id>/', views.update_rendezvous, name='update_rdv'),






    #saad
path('notaryhome/',notaryhome, name='notaryhome'),
path('notary_register/', NotaryRegisterView.as_view(), name='notary_register'),
path('nclients/', views.display_nclients, name='nclients'),
path('pnclients/', views.pnclients, name='pnclients'),
path('upnclient/<int:client_id>/', views.update_nclient, name='update_nclient'),
path('delete_nclients/<int:cid>/', views.delete_nclient, name='delete_nclients'),
path('nrdv/', views.nrendezvous_list, name='nrdv'),
path('prdv/', views.prdv, name='prdv'),
path('pnrdv/', views.pnrdv, name='pnrdv'),
path('upnrdv/<int:rdv_id>/', views.update_nrendezvous, name='update_nrdv'),
path('delete_rdvs/<int:cid>/', views.delete_rdv, name='delete_rdvs'),

path('delete_nrdvs/<int:cid>/', views.delete_nrdv, name='delete_nrdvs'),
path('npaiements/', views.npaiement, name='npaiements'),
path('tablenpaiement/', views.tablenpaiement, name='tablenpaiement'),
path('delete_npaiement/<int:cid>/', views.delete_npaiement, name='delete_npaiement'),
path('upnpaiement/<int:npaiement_id>/', views.update_npaiement, name='upnpaiement'),
path('contrats/', views.contrats, name='contrats'),
path('vente/', views.generate_word_document, name='vente'),
path('ventecycle/', views.vente_cycle, name='ventecycle'),
path('ventecar/', views.vente_car, name='ventecar'),
path('dette/', views.dette, name='dette'),
path('affaire/', views.affairepage, name='affaire'),
path('delete_affaire/<int:cid>/', views.delete_affaire, name='delete_affaire'),
path('rdv/', views.rendezvous_list, name='rdv'),
path('upjugements/<int:jugement_id>/', views.upjugements, name='upjugements'),
path('manage_clients_notary/', views.manage_clients_notary, name='manage_clients_notary'),
path('printnpaiement/<int:npaiement_id>/', views.printnpaiement, name='printnpaiement'),

]
