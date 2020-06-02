# Description: Substition method build a table with random ordered alphabet, and collects encrypted message by this table.
# Example:
# Table: {A: E, B: F, C: D, O: Z}"
# BOB -> FZF
# ------------------------------

# Actions hash to call appropriate function dependent on action id.
# __Encrypt/Decrypt are Procs(lambdas)
@actions = {
  'encrypt' => ->(message, alphabet){ message.chars.map { |el| alphabet[el] }.join }
}

def __main__ # Entrypoint
  # Input function.
  # __Gets message, cipher step and action id
  def __input__
    print "What's the message: "
    message = gets.chomp.upcase
    def alphabet(error = nil)
      puts "ERROR: #{error}" if error

      print "What's the alphabet string. Default: 'ZYXWVUTSRQPONMLKJIHGFEDCBA': "
      alphabet_str = gets.chomp.upcase # Gets alphabe string

      # Errors
      alphabet("Alphabet length is not 26 letters! Try again.") if alphabet_str.length != 26 and alphabet_str.length != 0 # Tries again when alphabet length is not 26
      alphabet("Alphabet letters must be unique! Try again.") if alphabet_str.chars.uniq.length != alphabet_str.length # Tries again when repeated letters detected
      alphabet("Alphabet is in it's correct order! Enter inordered alphabet. ") if alphabet_str === "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      alphabet_str = "ZYXWVUTSRQPONMLKJIHGFEDCBA" if alphabet_str.length === 0 # Sets default value when input is empty
      
      alphabet_str
    end

    # Action id input function. Used to recursively call when wrong user input.
    def action(error = nil)
      puts "ERROR: #{error}" if error

      print "What action you'd like to run? \n[0] Encrypt\n[1] Decrypt\n> "
      action = /^[^\d]*(\d+)/.match(gets.chomp)[1].to_i
      action("Please input correct action id. Options are 0 and 1") if action > 1 # Call action input method again if action id is not correct
      action
    end

    alphabet_str = alphabet
    action_val = action

    alphabet_ordered = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_hash = {}
    if action_val === 1
      alphabet_ordered.chars.each_with_index{ |el, index| alphabet_hash[el] = alphabet_str[index] }
    else
      alphabet_str.chars.each_with_index{ |el, index| alphabet_hash[el] = alphabet_ordered[index] }
    end

    return message, alphabet_hash, action_val
  end

  message, alphabet, action = __input__ # Save variables from STDIN
  result = @actions['encrypt'].(message, alphabet) # Call appropriate Proc

  puts "Result: #{result}"
end
__main__
