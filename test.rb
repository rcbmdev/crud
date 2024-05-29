# encoding: utf-8
require 'stripe'

# Configure a chave sdecreta do Stripe
Stripe.api_key = "sk_test_51PBm7E2LSm9FOqxFwBZchpf0Orl4yebUn3WCKWO5WSXJ6UrptLa42LQipOGXSG4OiBtoFCCVEXACbt21nFkYWUcQ00ekr3Fsyc"

# Criar um novo checkout session
checkout_session = Stripe::Checkout::Session.create(
  payment_method_types: ['card'],
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: {
        name: 'Exemplo de Produto',
        images: ['https://via.placeholder.com/150'],
      },
      unit_amount: 1000, # Valor em centavos
    },
    quantity: 1,
  }],
  mode: 'payment',
  success_url: 'https://seusite.com/sucesso',
  cancel_url: 'https://seusite.com/cancelado',
)

# Redirecionar para a URL de checkout
puts checkout_session.url
