import argparse
from Reader.Factory import get_reader_instance
from Writer.Factory import get_writer_instance
from Processor.Factory import get_processor_instance
from Logger.Factory import get_logger_instance

def main():
    parser = argparse.ArgumentParser(description="Multi-Pathway File Processor")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--isCodeA', action='store_true', help="Use CodeA components")
    group.add_argument('--isCodeB', action='store_true', help="Use CodeB components")
    args = parser.parse_args()

    code_type = "A" if args.isCodeA else "B"
    logger = get_logger_instance(code_type)

    reader = get_reader_instance(code_type, logger)
    writer = get_writer_instance(code_type, logger)
    processor = get_processor_instance(code_type, logger)

    input_file = "input.txt" if code_type == "A" else "input.csv"
    output_file = "output.txt" if code_type == "A" else "output.csv"

    try:
        data = reader.read(input_file)
        processed_data = processor.process(data)
        writer.write(output_file, processed_data)
        logger.log("Pipeline completed successfully.")
    except Exception as e:
        logger.log(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
