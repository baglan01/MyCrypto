# Description: Caesar encryption method shifts string characters by N step.
# Example: ABC+3 = DEF
# ------------------------------

# Actions hash to call appropriate function dependent on action id.
# __Encrypt/Decrypt are Procs(lambdas).
@actions = {
  'encrypt' => ->(message, step){ message.bytes.map { |el| ((el+step)%255).chr }.join },
  'decrypt' => ->(message, step){ message.bytes.map { |el| ((el-step)%255).chr }.join }
}

def __main__ # Entrypoint
  # Input function.
  # __Gets message, cipher step and action id
  def __input__
    print "What's the message: "
    message = gets.chomp
    print "What's the step: "
    step = /^[^\d]*(\d+)/.match(gets.chomp)[1].to_i # Gets first integer from string using RegEx (To avoid wrong input)

    # Action id input function. Used to recursively call when wrong user input.
    def action(error = nil)
      puts "ERROR: #{error}" if error
      print "What action you'd like to run? \n[0] Encrypt\n[1] Decrypt\n> "
      action_str = /^[^\d]*(\d+)/.match(gets.chomp)[1].to_i
      action("Please input correct action id. Options are 0 and 1") if(action_str > 1) # Call action input method again if action id is not correct
      action
    end

    message, step, action
  end

  message, step, action = __input__ # Save variables from STDIN
  result = @actions[(action === 1 ? 'encrypt' : 'decrypt')].(message, step) # Call appropriate Proc

  puts "Result: #{result}"
end
__main__
