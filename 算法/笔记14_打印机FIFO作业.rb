class PrintManager

	def initialize
		@queue = []
	end

	def queue_print_job(document)
		@queue.push(document)
	end

	def run
		while @queue.any?
			# Ruby的shift方法可移出并返回数组的第一个元素
			print(@queue.shift)
		end

		private

		def print(document)
			puts document
		end
	end

# test
print_manager = PrintManager.new 
print_manager.queue_print_job("First Document") 
print_manager.queue_print_job("Second Document") 
print_manager.queue_print_job("Third Document") 
print_manager.run

# First Document
# Second Document
# Third Document