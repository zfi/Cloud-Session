/**
 * This class is generated by jOOQ
 */
package com.parallax.server.common.cloudsession.db.generated;


import com.parallax.server.common.cloudsession.db.generated.tables.Authenticationtoken;
import com.parallax.server.common.cloudsession.db.generated.tables.Authenticationtokenchallenge;
import com.parallax.server.common.cloudsession.db.generated.tables.Bucket;
import com.parallax.server.common.cloudsession.db.generated.tables.Confirmtoken;
import com.parallax.server.common.cloudsession.db.generated.tables.Resettoken;
import com.parallax.server.common.cloudsession.db.generated.tables.User;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.annotation.Generated;

import org.jooq.Table;
import org.jooq.impl.SchemaImpl;


/**
 * This class is generated by jOOQ.
 */
@Generated(
	value = {
		"http://www.jooq.org",
		"jOOQ version:3.6.1"
	},
	comments = "This class is generated by jOOQ"
)
@SuppressWarnings({ "all", "unchecked", "rawtypes" })
public class Cloudsession extends SchemaImpl {

	private static final long serialVersionUID = 845918999;

	/**
	 * The reference instance of <code>cloudsession</code>
	 */
	public static final Cloudsession CLOUDSESSION = new Cloudsession();

	/**
	 * No further instances allowed
	 */
	private Cloudsession() {
		super("cloudsession");
	}

	@Override
	public final List<Table<?>> getTables() {
		List result = new ArrayList();
		result.addAll(getTables0());
		return result;
	}

	private final List<Table<?>> getTables0() {
		return Arrays.<Table<?>>asList(
			Authenticationtoken.AUTHENTICATIONTOKEN,
			Authenticationtokenchallenge.AUTHENTICATIONTOKENCHALLENGE,
			Bucket.BUCKET,
			Confirmtoken.CONFIRMTOKEN,
			Resettoken.RESETTOKEN,
			User.USER);
	}
}
