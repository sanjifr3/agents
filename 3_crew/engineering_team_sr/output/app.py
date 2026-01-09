import gradio as gr
from accounts import Account, get_share_price

# Initialize a single account for the demo
account = None

def create_account(initial_deposit):
    global account
    try:
        initial_deposit = float(initial_deposit)
        if initial_deposit < 0:
            return "Error: Initial deposit must be non-negative", ""
        account = Account(initial_deposit)
        return f"Account created successfully with initial deposit: ${initial_deposit:.2f}", get_account_summary()
    except ValueError:
        return "Error: Invalid amount", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

def deposit_funds(amount):
    global account
    if account is None:
        return "Error: Please create an account first", ""
    try:
        amount = float(amount)
        account.deposit(amount)
        return f"Successfully deposited ${amount:.2f}", get_account_summary()
    except ValueError:
        return "Error: Invalid amount", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

def withdraw_funds(amount):
    global account
    if account is None:
        return "Error: Please create an account first", ""
    try:
        amount = float(amount)
        account.withdraw(amount)
        return f"Successfully withdrew ${amount:.2f}", get_account_summary()
    except ValueError:
        return "Error: Invalid amount", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

def buy_shares(symbol, quantity):
    global account
    if account is None:
        return "Error: Please create an account first", ""
    try:
        symbol = symbol.upper().strip()
        quantity = int(quantity)
        price = get_share_price(symbol)
        account.buy_shares(symbol, quantity)
        return f"Successfully bought {quantity} shares of {symbol} at ${price:.2f} each", get_account_summary()
    except ValueError:
        return "Error: Invalid quantity", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

def sell_shares(symbol, quantity):
    global account
    if account is None:
        return "Error: Please create an account first", ""
    try:
        symbol = symbol.upper().strip()
        quantity = int(quantity)
        price = get_share_price(symbol)
        account.sell_shares(symbol, quantity)
        return f"Successfully sold {quantity} shares of {symbol} at ${price:.2f} each", get_account_summary()
    except ValueError:
        return "Error: Invalid quantity", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

def get_account_summary():
    global account
    if account is None:
        return "No account created yet"
    
    summary = f"💰 Cash Balance: ${account.get_cash_balance():.2f}\n"
    summary += f"📊 Portfolio Value: ${account.get_portfolio_value():.2f}\n"
    summary += f"💼 Total Account Value: ${account.get_total_value():.2f}\n"
    summary += f"📈 Profit/Loss: ${account.get_profit_loss():.2f}\n"
    return summary

def get_holdings():
    global account
    if account is None:
        return "No account created yet"
    
    holdings = account.get_holdings()
    if not holdings:
        return "No shares held"
    
    result = "Current Holdings:\n" + "="*50 + "\n"
    for symbol, quantity in holdings.items():
        price = get_share_price(symbol)
        value = quantity * price
        result += f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}\n"
    return result

def get_transactions():
    global account
    if account is None:
        return "No account created yet"
    
    transactions = account.get_transactions()
    if not transactions:
        return "No transactions yet"
    
    result = "Transaction History:\n" + "="*50 + "\n"
    for i, txn in enumerate(transactions, 1):
        result += f"{i}. {txn}\n"
    return result

def refresh_display():
    return get_account_summary(), get_holdings(), get_transactions()

def get_current_prices():
    symbols = ["AAPL", "TSLA", "GOOGL"]
    result = "Current Share Prices:\n" + "="*50 + "\n"
    for symbol in symbols:
        price = get_share_price(symbol)
        result += f"{symbol}: ${price:.2f}\n"
    return result

# Create Gradio Interface
with gr.Blocks(title="Trading Simulation Platform", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📊 Trading Simulation Platform")
    gr.Markdown("A simple account management system for trading simulation")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🏦 Account Management")
            
            with gr.Group():
                gr.Markdown("**Create Account**")
                initial_deposit_input = gr.Number(label="Initial Deposit ($)", value=10000)
                create_btn = gr.Button("Create Account", variant="primary")
                create_output = gr.Textbox(label="Status", lines=2)
            
            with gr.Group():
                gr.Markdown("**Deposit/Withdraw**")
                amount_input = gr.Number(label="Amount ($)")
                with gr.Row():
                    deposit_btn = gr.Button("Deposit")
                    withdraw_btn = gr.Button("Withdraw")
                transaction_output = gr.Textbox(label="Status", lines=2)
            
            with gr.Group():
                gr.Markdown("**Trade Shares**")
                symbol_input = gr.Textbox(label="Symbol (AAPL, TSLA, GOOGL)", value="AAPL")
                quantity_input = gr.Number(label="Quantity", value=1)
                with gr.Row():
                    buy_btn = gr.Button("Buy", variant="primary")
                    sell_btn = gr.Button("Sell", variant="stop")
                trade_output = gr.Textbox(label="Status", lines=2)
            
            refresh_btn = gr.Button("🔄 Refresh Display", variant="secondary")
        
        with gr.Column(scale=1):
            gr.Markdown("### 📈 Account Overview")
            
            account_summary = gr.Textbox(label="Account Summary", lines=6, interactive=False)
            
            holdings_display = gr.Textbox(label="Holdings", lines=8, interactive=False)
            
            prices_display = gr.Textbox(label="Current Prices", lines=5, interactive=False, value=get_current_prices())
            
            transactions_display = gr.Textbox(label="Transaction History", lines=10, interactive=False)
    
    # Event handlers
    create_btn.click(
        fn=create_account,
        inputs=[initial_deposit_input],
        outputs=[create_output, account_summary]
    ).then(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )
    
    deposit_btn.click(
        fn=deposit_funds,
        inputs=[amount_input],
        outputs=[transaction_output, account_summary]
    ).then(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )
    
    withdraw_btn.click(
        fn=withdraw_funds,
        inputs=[amount_input],
        outputs=[transaction_output, account_summary]
    ).then(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )
    
    buy_btn.click(
        fn=buy_shares,
        inputs=[symbol_input, quantity_input],
        outputs=[trade_output, account_summary]
    ).then(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )
    
    sell_btn.click(
        fn=sell_shares,
        inputs=[symbol_input, quantity_input],
        outputs=[trade_output, account_summary]
    ).then(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )
    
    refresh_btn.click(
        fn=refresh_display,
        inputs=[],
        outputs=[account_summary, holdings_display, transactions_display]
    )

if __name__ == "__main__":
    demo.launch()